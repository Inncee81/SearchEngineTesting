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

# test on firefox using explicit wait
result = 0
driver = webdriver.Firefox()

for i in range(1,10):
	driver.implicitly_wait(3)
	driver.get(testURL)
	inputElem = driver.find_element_by_id('query')
	inputElem.send_keys(searchKeyword)
	inputElem.send_keys(Keys.RETURN)

	submitStartTime = time.time()

	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nx_query")))
	renderEndTime = time.time()

	responseTime = renderEndTime - submitStartTime
	result += responseTime
	time.sleep(random.randint(1,5))

result = result/10
print(result)

# test on firefox using javascript
urlList = ["http://www.naver.com", "http://www.daum.net", "http://www.google.com", "http://www.yahoo.com"]

def findSearchTagID(pageSource):
	soup = BeautifulSoup(pageSource, 'html.parser')
	inputTagList = soup.find_all('input')

	for inputTag in inputTagList:
		if inputTag['type']=='search' or inputTag['type'] == 'text':
			if inputTag['id'] != None:
				return inputTag['id']

	return ""

for url in urlList:
	driver.get(url)
	html = driver.page_source

	searchTagID = findSearchTagID(html)

	if len(searchTagID) > 0:
		inputElem = driver.find_element_by_id(searchTagID)
		inputElem.send_keys(searchKeyword)
		inputElem.send_keys(Keys.RETURN)

		submitStartTime = time.time()

		WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nx_query")))
		renderEndTime = time.time()

		responseTime = renderEndTime - submitStartTime