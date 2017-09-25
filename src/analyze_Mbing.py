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
js_pageLoadTime = "return performance.timing.loadEventEnd - performance.timing.domLoading;"
js_networkTime = "return performance.timing.responseEnd - performance.timing.fetchStart;"
js_redirectTime = "return performance.timing.fetchStart - performance.timing.navigationStart"
## must start adb-server : "adb start-server" on cmd

#options = webdriver.ChromeOptions()
#options.add_experimental_option('androidPackage', 'com.android.chrome')
#options.add_argument("--incognito")
#driver = webdriver.Chrome(chrome_options=options)



keyword = "갤럭시노트8"

testURL = "http://www.bing.com"
searchTagID = "sb_form_q"

totalTime = 0
networkTime = 0
pageLoadTime = 0
redirectTime = 0

for i in range(0,5):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--incognito")

	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.get(testURL)

	time.sleep(5)

	inputElement = driver.find_element_by_id(searchTagID)
	inputElement.send_keys(keyword)
	time.sleep(3)

	inputElement.send_keys(Keys.RETURN)

	time.sleep(10)

	totalTime += driver.execute_script(js_totalTime)
	networkTime += driver.execute_script(js_networkTime)
	pageLoadTime += driver.execute_script(js_pageLoadTime)
	redirectTime += driver.execute_script(js_redirectTime)
	driver.close()



print("* BING -------------------")
print("Total Time : ", totalTime/5)
print("Redirect Time : ", redirectTime/5)
print("Network Time : ", networkTime/5)
print("Page Loading Time : ", pageLoadTime/5)
print("--------------------------")

testURL = "http://www.google.com"
searchTagID = "lst-ib"

time.sleep(5)

totalTime = 0
networkTime = 0
pageLoadTime = 0
redirectTime = 0

for i in range(0,5):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--incognito")

	driver = webdriver.Chrome(chrome_options=chrome_options)

	driver.get(testURL)
	inputElement = driver.find_element_by_id(searchTagID)
	inputElement.send_keys(keyword)
	time.sleep(3)

	inputElement.send_keys(Keys.RETURN)

	time.sleep(10)

	totalTime += driver.execute_script(js_totalTime)
	networkTime += driver.execute_script(js_networkTime)
	pageLoadTime += driver.execute_script(js_pageLoadTime)
	redirectTime += driver.execute_script(js_redirectTime)
	driver.close()

print("* GOOGLE -------------------")
print("Total Time : ", totalTime/5)
print("Redirect Time : ", redirectTime/5)
print("Network Time : ", networkTime/5)
print("Page Loading Time : ", pageLoadTime/5)
print("--------------------------")
