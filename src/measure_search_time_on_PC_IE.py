from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import matplotlib


#searchTagIDDict = {"http://www.daum.net":"query_totalsearch","http://www.baidu.com":"index-kw", "http://www.google.com":"lst-ib", "http://www.bing.com":"sb_form_q", "http://www.naver.com":"query", "http://www.yahoo.co.jp":"srchtxt"}
searchTagIDDict = {
"http://www.naver.com":"query", 
"http://www.daum.net":"q", 
"http://www.nate.com":"q",
"http://www.baidu.com":"kw", 
"http://www.google.com":"lst-ib", 
"http://www.bing.com":"sb_form_q", 
"http://www.yahoo.co.jp":"srchtxt"
}

keyword = "미세먼지"
timeDataFrame = pd.DataFrame()

searchingTimeSC = "return performance.timing.loadEventEnd - performance.timing.navigationStart;"
networkTimeSC = "return performance.timing.responseEnd - performance.timing.fetchStart;"
domLoadTimeSC = "return performance.timing.loadEventStart - performance.timing.domLoading;"
pageLoadTimeSC = "return performance.timing.loadEventEnd - performance.timing.loadEventStart;"


####################################################################################################################
##	* testOnIe : 크롬에서 웹사이트에 접속하여 검색 시간 측정
##	- url : 웹 사이트 주소
##	- searchTag : 검색 input tag id
## 	- searchkeyword : 검색 키워드
####################################################################################################################
def testOnIe(url, searchTag, searchkeyword):
	global timeDataFrame
	driver = webdriver.Ie()

	driver.get(url)
	time.sleep(15)

	inputElement = driver.find_element_by_id(searchTag)
	
	inputElement.send_keys(keyword)
	inputElement.send_keys(Keys.RETURN)

	time.sleep(15)

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

	driver.quit()

	timeDataFrame = timeDataFrame.append({'url':url,'searchTime':searchingTime,'networkTime':networkTime,'domLoadTime':domLoadTime,'pageLoadTime':pageLoadTime}, ignore_index=True)

if __name__ == "__main__":
	for i in range(0, 30):
		for key, value in searchTagIDDict.items():
			testOnIe(key, value, keyword)

		#with open('../csv/P_I_searchTime_result.csv', 'a') as f:
    	#	timeDataFrame.to_csv(f, header=False)

    	#timeDataFrame = pd.DataFrame()
	timeDataFrame.to_csv('../csv/P_I_searchTime_result.csv')
