from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup
import json
import subprocess as sub
import os
import signal


## Todo : measure the mean(total packet rtt)
def measureRTT(filePath):
	analyzeProcess = sub.Popen(('tcptrace','-r','-lW',filePath),stdout = sub.PIPE)
	out, err = analyzeProcess.communicate()

	connectionList = out.split("================================")

	## clear connectionList[0] Data - remove unnecessary data
	connectionList[0] = connectionList[0].split("TCP connections traced:")[1]

	resultDictList = []

	for i in range(0, len(connectionList)):
		connection = connectionList[i]
		resultDict = {}

		lineData = connection.split("\n")
		count = 0

		hostA = lineData[2].split()[2]
		hostA = hostA.split(":")[0]
		hostB = lineData[3].split()[2]
		hostB = hostB.split(":")[0]

		rttAvgAtoB = 0
		rttAvgBtoA = 0
		rttMinAtoB = 0
		rttMinBtoA = 0
		rttMaxAtoB = 0
		rttMaxBtoA = 0
		rttSample = 0

		for line in lineData:
			splitedLine = line.split()
			if 'RTT samples:' in line:
				rttSample = int(splitedLine[2])
			if 'RTT max:' in line:
				rttMaxAtoB = float(splitedLine[2])
				rttMaxBtoA = float(splitedLine[6])
			if 'RTT avg:' in line:
				rttAvgAtoB = float(splitedLine[2])
				rttAvgBtoA = float(splitedLine[6])
			if 'RTT min:' in line:
				rttMinAtoB = float(splitedLine[2])
				rttMinBtoA = float(splitedLine[6])

		resultDict = {'hostA':hostA, 'hostB':hostB, 'rttSample' : rttSample,'rttAvgAtoB':rttAvgAtoB, 'rttAvgBtoA':rttAvgBtoA, 'rttMinAtoB':rttMinAtoB, 'rttMinBtoA':rttMinBtoA, 'rttMaxAtoB':rttMaxAtoB, 'rttMaxBtoA':rttMaxBtoA}

		check = False
		if len(resultDictList) == 0:
			resultDictList.append(resultDict)
			check = True
		else:
			for dictionary in resultDictList:
				if dictionary['hostA'] == hostA and dictionary['hostB'] == hostB:
					dictionary['rttMinAtoB'] = min([rttMinAtoB, dictionary['rttMinAtoB']])
					dictionary['rttMinBtoA'] = min([rttMinBtoA, dictionary['rttMinBtoA']])
					dictionary['rttMaxAtoB'] = max([rttMaxAtoB, dictionary['rttMinAtoB']])
					dictionary['rttMaxBtoA'] = max([rttMaxBtoA, dictionary['rttMaxBtoA']])
					dictionary['rttAvgAtoB'] = (dictionary['rttSample']*dictionary['rttAvgAtoB']+rttSample*rttAvgAtoB)/(rttSample+dictionary['rttSample'])
					dictionary['rttSample'] += rttSample
					check = True
					break

		if check == False:
			resultDictList.append(resultDict)

	for i in resultDictList:
		print(i)

def confirmConnectionIP(filePath):
	analyzeProcess = sub.Popen(('tcptrace','-r','-lW',filePath),stdout = sub.PIPE)
	out, err = analyzeProcess.communicate()

	connectionList = out.split("================================")

	## clear connectionList[0] Data - remove unnecessary data
	connectionList[0] = connectionList[0].split("TCP connections traced:")[1]

	connectionDictList = []

	for connection in connectionList:
		count = 0

		lineList = connection.split("\n")
		connectionInfoDict = {}

		hostA = lineList[2].split()[2]
		hostA = hostA.split(":")[0]
		hostB = lineList[3].split()[2]
		hostB = hostB.split(":")[0]

		connectionInfoDict['hostA'] = hostA
		connectionInfoDict['hostB'] = hostB

		for line in lineList:
			# first packet time
			# last packet time
			# total packets
			# RTT min, max, avg
			if "first packet:" in line:
				fp_time = line[16:]
			if "last packet:" in line:
				lp_time = line[16:]
			if "total packets:" in line:
				splitedLine = line.split("total packets:")
				if len(splitedLine) == 3:
					totalPackets = int(splitedLine[1])
			if "RTT min:" in line:
				splitedLine = line.split()
				rttMinAtoB = float(splitedLine[2])
				rttMinBtoA = float(splitedLine[6])
			if "RTT max:" in line:
				splitedLine = line.split()
				rttMaxAtoB = float(splitedLine[2])
				rttMaxBtoA = float(splitedLine[6])
			if "RTT avg:" in line:
				splitedLine = line.split()
				rttAvgAtoB = float(splitedLine[2])
				rttAvgBtoA = float(splitedLine[6])

		connectionInfoDict['first_packet_time'] = fp_time
		connectionInfoDict['last_packet_time'] = lp_time
		connectionInfoDict['total_packets'] = totalPackets
		connectionInfoDict['RTT_min'] = rttMinAtoB
		connectionInfoDict['RTT_max'] = rttMaxAtoB
		connectionInfoDict['RTT_avg'] = rttAvgAtoB

		connectionDictList.append(connectionInfoDict)

	return connectionDictList

	

## Todo : calculate search query time
if __name__ == "__main__":
	testURL = "http://www.naver.com"
	searchKeyword = "pokemon"
	#urlList = ["http://www.naver.com", "http://www.nate.com", "http://www.baidu.com", "http://www.google.com", "http://www.bing.com"]

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--incognito")
	driver = webdriver.Chrome(chrome_options=chrome_options)

	## Capture packet
	print("** capture packet ** start---------------------------------")

	#
	

	## connect to testURL
	driver.get(testURL)

	## Todo : submit searching keyword
	inputElement = driver.find_element_by_id('query')

	inputElement.send_keys(searchKeyword)
	time.sleep(2)
	#p = sub.Popen(('tcpdump', '-l', '-i', 'wlp1s0','-w','./tcpdump_packetData/baidu_packet.dump'), stdout=sub.PIPE)
	p = sub.Popen(('tcpdump', '-l', '-i', 'wlp1s0'), stdout=sub.PIPE)
	inputElement.send_keys(Keys.RETURN)

	time.sleep(2)
	driver.close()
	time.sleep(3)

	## Todo : terminate
	os.kill(p.pid, signal.SIGINT)
	
	for row in iter(p.stdout.readline,b''):
		print(row.rstrip())
		
	print("** capture packet ** end---------------------------------")


	## measure the mean(total packet rtt)
	#rttOntestURL = measureRTT('./tcpdump_packetData/baidu_packet.dump')

	## get server query response time
	#server_query_response_time = rttOntestURL-networkLatency

	## get connection List and check
	#result = confirmConnectionIP('./tcpdump_packetData/naver_packet.dump')
	#for i in result:
	#	print(i)