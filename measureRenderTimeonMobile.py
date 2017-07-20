from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup


testURL = "https://www.naver.com"
searchKeyword = "keyword"

## Todo : measure web rendering time on mobile system using javascript
driver  = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.ANDROID)

#driver.get(testURL)
#inputElem = driver.find_element_by_id('query')

#inputElem.send_keys(searchKeyword)
#inputElem.send_keys(Keys.RETURN)
#submitStartTime = time.time()
#time.sleep(0.5)

## page loading time
#driver.execute_script("var result = 0; window.onload = function(){var now = new Date().getTime(); result = now - performance.timing.navigationStart;}")

#print("render start time : ", submitStartTime)
#print("render end time : ", renderEndTime)

#print(renderEndTime-submitStartTime)

##Todo : measure response time on mobile web using explicit wait in selenium
#driver.get(testURL)
#inputElem = driver.find_element_by_id('query')
#inputElem.send_keys(searchKeyword)
#inputElem.send_keys(Keys.RETURN)
#submitStartTime = time.time()

# Timeout: 10s 
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nx_query")))
#renderEndTime = time.time()

#responseTime = renderEndTime - submitStartTime

urlList = ["http://www.naver.com", "http://www.daum.net", "http://www.google.com", "http://www.yahoo.com"]
nextIDList = ['nx_query','q','lst-ib','yschsp']


def findSearchTagID(pageSource):
	soup = BeautifulSoup(pageSource, 'html.parser')
	inputTagList = soup.find_all('input')

	for inputTag in inputTagList:
		if inputTag['type']=='search' or inputTag['type'] == 'text':
			if inputTag['id'] != None:
				return inputTag['id']

	return ""



dict = {"naver":0, "daum":0, "google":0, "yahoo":0}

for j in range(0,10):
	for i in range(0, len(urlList)):
		url = urlList[i]
		print(url)
		driver.get(url)
		time.sleep(2)
		html = driver.page_source

		searchTagID = findSearchTagID(html)
		print("submit id : ", searchTagID)

		if len(searchTagID) > 0:
			inputElem = driver.find_element_by_id(searchTagID)
			inputElem.send_keys(searchKeyword)
			inputElem.send_keys(Keys.RETURN)

			submitStartTime = time.time()

			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, nextIDList[i])))
			renderEndTime = time.time()

			responseTime = renderEndTime - submitStartTime

			if i == 0:
				dict["naver"] += responseTime
			if i == 1:
				dict["daum"] += responseTime
			if i == 2:
				dict["google"] += responseTime
			if i == 3:
				dict["yahoo"] += responseTime

		time.sleep(1)

print("average of rendering time on NAVER = ", dict["naver"]/10)
print("average of rendering time on DAUM = ", dict["daum"]/10)
print("average of rendering time on GOOGLE = ", dict["google"]/10)
print("average of rendering time on YAHOO = ", dict["yahoo"]/10)