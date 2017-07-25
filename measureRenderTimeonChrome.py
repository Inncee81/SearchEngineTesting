from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup

def findSearchTagID(pageSource):
	soup = BeautifulSoup(pageSource, 'html.parser')
	inputTagList = soup.find_all('input')

	for inputTag in inputTagList:
		if inputTag['type']=='search' or inputTag['type'] == 'text':
			if inputTag['id'] != None:
				return inputTag['id']

	return ""

urlList = ["http://www.naver.com", "http://www.daum.net","http://www.nate.com", "http://www.baidu.com", "http://www.google.com", "http://www.yahoo.com"]
keywordList = ["spiderman", "daejeon", "pokemon"]
searchTagIDList = {"http://www.naver.com":"query", "http://www.daum.net":"q", "http://www.nate.com":"q","http://www.baidu.com":"kw", "http://www.google.com":"lst-ib", "http://www.yahoo.com":"uh-search-box"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)

## 브라우저 시크릿 모드로 실행 
## 한 keyword로 urlList의 모든 페이지에서 1000번 검색 후 시간 측정

jsSourceCode = "return performance.timing.loadEventEnd - performance.timing.navigationStart;"

for url in urlList:
	print(url)
	for keyword in keywordList:
		result = 0

		for i in range(0,100):
			driver.get(url)

			searchTagID = searchTagIDList[url]

			inputElem = driver.find_element_by_id(searchTagID)
			inputElem.send_keys(keyword)
			inputElem.send_keys(Keys.RETURN)

			renderingTime = driver.execute_script(jsSourceCode)
			result += renderingTime
			time.sleep(1)

		print(keyword," : ", result/100)













#driver.get("http://www.naver.com")

#inputElem = driver.find_element_by_id('query')
#inputElem.send_keys("defcon")
#inputElem.send_keys(Keys.RETURN)

#submitStartTime = time.time()

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nx_query")))
#renderEndTime = time.time()

#responseTime = renderEndTime - submitStartTime
#print(responseTime)

