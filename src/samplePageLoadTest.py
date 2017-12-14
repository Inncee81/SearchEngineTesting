from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import matplotlib

timeDataFrame = pd.DataFrame()

searchingTimeSC = "return performance.timing.loadEventEnd - performance.timing.navigationStart;"
networkTimeSC = "return performance.timing.responseEnd - performance.timing.fetchStart;"
pageLoadTimeSC = "return performance.timing.loadEventEnd - performance.timing.domLoading;"

for i in range(0, 10):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--incognito")
	driver = webdriver.Chrome(chrome_options=chrome_options)

	driver.get('http://192.168.1.109/example.php')
	time.sleep(5)

	searchingTime = driver.execute_script(searchingTimeSC)
	networkTime = driver.execute_script(networkTimeSC)
	pageLoadTime = driver.execute_script(pageLoadTimeSC)

	driver.quit()

	timeDataFrame = timeDataFrame.append({'plt':searchingTime,'networkTime':networkTime,'computationTime':pageLoadTime}, ignore_index=True)

timeDataFrame.to_csv('../csv/samplePageLoadTest.csv')