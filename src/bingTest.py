from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import matplotlib

keyword = "미세먼지"
timeDataFrame = pd.DataFrame()
url = "http://www.bing.com"

searchingTimeSC = "return performance.timing.loadEventEnd - performance.timing.navigationStart;"
networkTimeSC = "return performance.timing.responseEnd - performance.timing.fetchStart;"
domLoadTimeSC = "return performance.timing.loadEventStart - performance.timing.domLoading;"
pageLoadTimeSC = "return performance.timing.loadEventEnd - performance.timing.loadEventStart;"

for i in range(0,30):
	firefox_profile = webdriver.FirefoxProfile()
	firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
	driver = webdriver.Firefox(firefox_profile=firefox_profile)

	driver.get(url)
	time.sleep(5)

	inputElement = driver.find_element_by_id('sb_form_q')
	
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

	timeDataFrame = timeDataFrame.append({'url':url,'searchTime':searchingTime,'networkTime':networkTime,'domLoadTime':domLoadTime,'pageLoadTime':pageLoadTime}, ignore_index=True)
	driver.quit()

timeDataFrame.to_csv('../csv/bing_time_measurement.csv')
