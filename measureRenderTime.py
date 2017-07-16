from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

testURL = "http://www.naver.com"
searchKeyword = "keyword"

## Todo : measure web rendering time on mobile system
driver  = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.ANDROID)

driver.get(testURL)
inputElem = driver.find_element_by_id('query')
inputElem.send_keys(searchKeyword)
inputElem.send_keys(Keys.RETURN)

driver.execute_script("var page_loadTime;window.onload = function(){var now = new Date().getTime();page_loadTime = now - performance.timing.navigationStart;}")
result = driver.execute_script("return page_loadTime;")
print(result)

## Todo : measure web rendering time on PC
# test on chrome

# test on firefox