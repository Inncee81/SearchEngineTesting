from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup
import json

def findSearchTagID(pageSource):
	soup = BeautifulSoup(pageSource, 'html.parser')
	inputTagList = soup.find_all('input')

	for inputTag in inputTagList:
		if inputTag['type']=='search' or inputTag['type'] == 'text':
			if inputTag['id'] != None:
				return inputTag['id']

	return ""

urlList = ["http://www.naver.com", "http://www.daum.net","http://www.nate.com", "http://www.baidu.com", "http://www.google.com", "http://www.bing.com"]
keywordList = ["spiderman", "okja", "dunkirk"]
searchTagIDList = {"http://www.naver.com":"query", "http://www.daum.net":"q", "http://www.nate.com":"q","http://www.baidu.com":"kw", "http://www.google.com":"lst-ib", "http://www.bing.com":"sb_form_q"}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver",chrome_options=chrome_options)

## 브라우저 시크릿 모드로 실행 
## 한 keyword로 urlList의 모든 페이지에서 1000번 검색 후 시간 측정

jsSourceCode = "return performance.timing.loadEventEnd - performance.timing.requestStart;"
resultDict = {}
def testInURL(url):
	print(url)
	for keyword in keywordList:
		result = 0

		tmpList = []
		for i in range(0,50):
			driver.get(url)

			searchTagID = searchTagIDList[url]

			inputElem = driver.find_element_by_id(searchTagID)
			inputElem.send_keys(keyword)
			inputElem.send_keys(Keys.RETURN)

			renderingTime = driver.execute_script(jsSourceCode)

			tmpList.append(renderingTime)
			time.sleep(random.randint(1,5))
		
		keyName = url.split(".")[1]+"_"+keyword
		resultDict[keyName] = tmpList

		with open('chromeTest'+'_'+url.split(".")[1]+'.txt', 'w') as file:
			file.write(json.dumps(resultDict))


#for url in urlList:
#	testInURL(url)
	
testInURL("http://www.baidu.com")

#print(resultDict)


#with open('chromeTest', 'w') as file:
#     file.write(json.dumps(resultDict))

#with open('datacalc.txt', 'w') as file:
#     file.write(json.dumps(resultDict2))









#driver.get("http://www.naver.com")

#inputElem = driver.find_element_by_id('query')
#inputElem.send_keys("defcon")
#inputElem.send_keys(Keys.RETURN)

#submitStartTime = time.time()

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nx_query")))
#renderEndTime = time.time()

#responseTime = renderEndTime - submitStartTime
#print(responseTime)

