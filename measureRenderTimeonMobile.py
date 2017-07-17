from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC

testURL = "https://www.naver.com"
searchKeyword = "keyword"

## Todo : measure web rendering time on mobile system using javascript
driver  = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.ANDROID)

driver.get(testURL)
inputElem = driver.find_element_by_id('query')
inputElem.send_keys(searchKeyword)
inputElem.send_keys(Keys.RETURN)
submitStartTime = time.time()
time.sleep(0.5)

## page loading time
driver.execute_script("var result = 0; window.onload = function(){var now = new Date().getTime(); result = now - performance.timing.navigationStart;}")

print("render start time : ", submitStartTime)
print("render end time : ", renderEndTime)

print(renderEndTime-submitStartTime)

##Todo : measure response time on mobile web using explicit wait in selenium
driver.get(testURL)
inputElem = driver.find_element_by_id('query')
inputElem.send_keys(searchKeyword)
inputElem.send_keys(Keys.RETURN)
submitStartTime = time.time()

# Timeout: 10s 
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "nx_query")))
renderEndTime = time.time()

responseTime = renderEndTime - submitStartTime

## Todo : measure web rendering time on PC
# test on chrome

driver = webdriver.Chrome('C:\\Users\\miw52\\Downloads\\chromedriver_win32\\chromedriver')
driver.implicitly_wait(3)

driver.get("http://www.naver.com")


# test on firefox
driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get("http://www.python.org")
