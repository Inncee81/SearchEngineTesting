from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup
import json


keywordList = ["hangout", "kakaotalk", "facebook", "instagram", "twitter"]
jsSourceCode = "return performance.timing.loadEventEnd - performance.timing.requestStart;"
driver  = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.ANDROID)

def testOnMobileWebView(url, searchTagID):
	# resultDict : {"url_keyword":[searchingTimeList]}
	resultDict = {}
	urlKeyword = url.split(".")[1]

	for keyword in keywordList:
		# connect to mobile web view using selendroid
		
		driver.get(url)

		time.sleep(5)
		inputElement = driver.find_element_by_id(searchTagID)
		inputElement.send_keys(keyword)
		inputElement.send_keys(Keys.RETURN)

		time.sleep(5)

		# measure (loadEventEnd - requestStart) on url
		searchingTime = driver.execute_script(jsSourceCode)

		resultDict[urlKeyword+"_"+keyword] = []
		resultDict[urlKeyword+"_"+keyword].append(searchingTime)
		
		# 1) just string : log format = "[url]_keyword_searchingTime"
		# 2) json format = {"url_keyword":[searchingTimeList]}

	# write the result on file
	with open('result/mobileWebView.txt', 'a') as file:
		file.write(json.dumps(resultDict))


def findSearchTagID(pageSource):
	soup = BeautifulSoup(pageSource, 'html.parser')
	inputTagList = soup.find_all('input')

	for inputTag in inputTagList:
		if inputTag['type']=='search' or inputTag['type'] == 'text':
			if inputTag['id'] != None:
				return inputTag['id']

	return ""

def createSearchTagIDDict(urlList):
	searchTagIDDict = {}

	for url in urlList:
		driver.get(url)
		searchTagIDDict[url] = findSearchTagID(driver.page_source)

	return searchTagIDDict



if __name__ == "__main__":
	# test urls
	searchTagIDDict = {"http://www.daum.net":"query_totalsearch","http://www.baidu.com":"index-kw", "http://www.google.com":"lst-ib", "http://www.bing.com":"sb_form_q", "http://www.naver.com":"query"}
	urlList = ["http://www.daum.net","http://www.baidu.com", "http://www.google.com", "http://www.bing.com", "http://www.naver.com"]

	
	for key, value in searchTagIDDict.items():
		testOnMobileWebView(key, value)


	## Todo : measure time on mobile web view
	
	## Todo : measure time on mobile chrome
	# connect to mobile chrome using selenium