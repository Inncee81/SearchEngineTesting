from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup


result = 0
driver = webdriver.Chrome()
testURL = "http://www.naver.com"
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

# Compare rendering time between domestic web service and abroad web service
urlList = ["http://www.naver.com", "http://www.daum.net", "http://www.baidu.com", "http://www.google.com", "http://www.yahoo.com"]

## test using explicit wait
driver.get("http://www.naver.com")

inputElem = driver.find_element_by_id('query')
inputElem.send_keys("defcon")
inputElem.send_keys(Keys.RETURN)

submitStartTime = time.time()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nx_query")))
renderEndTime = time.time()

responseTime = renderEndTime - submitStartTime
print(responseTime)

## test using javascript
driver.get("http://www.naver.com")

inputElem = driver.find_element_by_id('query')
inputElem.send_keys("codegate")
inputElem.send_keys(Keys.RETURN)
submitTime = time.time()

jsSourceCode = 'return performance.timing.loadEventEnd - performance.timing.navigationStart;'
renderingTime = driver.execute_script(jsSourceCode)
print(renderingTime)


jsSourceCode = 'return performance.timing.loadEventEnd;'
loadingCompleteTime = driver.execute_script(jsSourceCode)
print(loadingCompleteTime)

print("submit Time : ", submitTime)
print("loading complete time : ", loadingCompleteTime)
print("duration Time : ", loadingCompleteTime-submitTime*1000)

print("renderingTime : ", renderingTime)
## 