from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup
import json


js_totalTime = "return performance.timing.loadEventEnd - performance.timing.navigationStart;"
js_pageLoadTime = "return performance.timing.loadEventEnd - performance.timing.responseEnd;"
js_networkTime = "return performance.timing.responseEnd - performance.timing.fetchStart;"
js_redirectTime = "return performance.timing.fetchStart - performance.timing.navigationStart"
## must start adb-server : "adb start-server" on cmd

options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.android.chrome')
options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=options)

keyword = "청년경찰"

testURL = "http://www.bing.com"
searchTagID = "sb_form_q"

driver.get(testURL)

time.sleep(5)

inputElement = driver.find_element_by_id(searchTagID)
inputElement.send_keys(keyword)
time.sleep(3)

inputElement.send_keys(Keys.RETURN)

time.sleep(5)

totalTime = driver.execute_script(js_totalTime)
networkTime = driver.execute_script(js_networkTime)
pageLoadTime = driver.execute_script(js_pageLoadTime)
redirectTime = driver.execute_script(js_redirectTime)

print("* BING -------------------")
print("Total Time : ", totalTime)
print("Redirect Time : ", redirectTime)
print("Network Time : ", networkTime)
print("Page Loading Time : ", pageLoadTime)
print("--------------------------")

testURL = "http://www.daum.net"
searchTagID = "query_totalsearch"

time.sleep(5)

driver.get(testURL)
inputElement = driver.find_element_by_id(searchTagID)
inputElement.send_keys(keyword)
time.sleep(3)

inputElement.send_keys(Keys.RETURN)

time.sleep(5)

totalTime = driver.execute_script(js_totalTime)
networkTime = driver.execute_script(js_networkTime)
pageLoadTime = driver.execute_script(js_pageLoadTime)
redirectTime = driver.execute_script(js_redirectTime)

print("* DAUM -------------------")
print("Total Time : ", totalTime)
print("Redirect Time : ", redirectTime)
print("Network Time : ", networkTime)
print("Page Loading Time : ", pageLoadTime)
print("--------------------------")

driver.close()