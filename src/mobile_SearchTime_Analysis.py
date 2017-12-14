## 검색시간 : performance.timing.loadEventEnd - performance.timing.navigationStart
## 네트워크 시간 : performance.timing.requestEnd - performance.timing.fetchStart
## 페이지 로딩 시간 : performance.timing.loadEventEnd - performance.timing.domLoading

### Mobile webdriver


### Mobile Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup
import json

searchTagIDDict = {"http://www.daum.net":"query_totalsearch","http://www.baidu.com":"index-kw", "http://www.google.com":"lst-ib", "http://www.bing.com":"sb_form_q", "http://www.naver.com":"query", "http://www.yahoo.co.jp":"p"}
keyword = "미세먼지"

searchingTimeSC = "return performance.timing.loadEventEnd - performance.timing.navigationStart;"
networkTimeSC = "return performance.timing.requestEnd - performance.timing.fetchStart;"
domLoadTimeSC = "return performance.timing.loadEventStart - performance.timing.domLoading;"
pageLoadTimeSC = "return performance.timing.loadEventEnd - performance.timing.loadEventStart;"

def testOnMobileChrome(url, searchTag, searchkeyword):
	options = webdriver.ChromeOptions()
	options.add_experimental_option('androidPackage', 'com.android.chrome')
	options.add_argument("--incognito")
	driver = webdriver.Chrome(chrome_options=options)

	driver.get(url)
	time.sleep(5)

	if 'yahoo' in url:
		inputElement = driver.find_element_by_name(searchTag)
	else:
		inputElement = driver.find_element_by_id(searchTag)
	
	inputElement.send_keys(keyword)
	inputElement.send_keys(Keys.RETURN)

	time.sleep(5)

		# measure (loadEventEnd - requestStart) on url
	searchingTime = driver.execute_script(searchingTimeSC)
	networkTime = driver.execute_script(networkTimeSC)
	domLoadTime = driver.execute_script(domLoadTimeSC)
	pageLoadTime = driver.execute_script(pageLoadTimeSC)

	print("------------------------------------------------------------")
	print("***",url,"***")
	print("검색 시간 : ", searchingTime)
	print("네트워크 시간 : ", networkTime)
	print("dom 로드 시간 : ", domLoadTime)
	print("페이지 로드 시간 : ", pageLoadTime)
	print("------------------------------------------------------------")

	driver.quit()


def findSearchTagID(pageSource):
	soup = BeautifulSoup(pageSource, 'html.parser')
	inputTagList = soup.find_all('input')

	for inputTag in inputTagList:
		if inputTag['type']=='search' or inputTag['type'] == 'text':
			if inputTag['id'] != None:
				return inputTag['id']

	return ""

if __name__ == "__main__":
	for key, value in searchTagIDDict.items():
		testOnMobileChrome(key, value, keyword)
