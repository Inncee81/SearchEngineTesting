from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup


keywordList = {"pokemon", "toeic", "weather", "melon"}
jsScript = "return performance.timing.loadEventEnd - performance.timing.requestStart;"

def testOnMobileWebView(url, searchTagID):
	# resultDict : {"url_keyword":[searchingTimeList]}
	resultDict = {}
	urlKeyword = url.split(".")[1]

	for keyword in keywordList:
		# connect to mobile web view using selendroid
		driver  = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.ANDROID)
		driver.get(url)

		time.sleep(2)
		inputElement = driver.find_element_by_id(searchTagID)
		inputElement.send_keys(keyword)
		inputElement.send_keys(Keys.RETURN)

		time.sleep(2)

		# measure (loadEventEnd - requestStart) on url
		searchingTime = driver.execute_script(jsSourceCode)

		resultDict[urlKeyword+"_"+keyword] = []
		resultDict[urlKeyword+"_"+keyword].append(searchingTime)

		
		# 1) just string : log format = "[url]_keyword_searchingTime"
		# 2) json format = {"url_keyword":[searchingTimeList]}

	# write the result on file
	with open('result/mobileWebView'+'_'+urlName+'.txt', 'w') as file:
		file.write(json.dumps(resultDict))



def testOnMobileChrome():


if __name__ == "__main__":
	# test urls
	searchTagIDDict = {"http://www.naver.com":"query", "http://www.daum.net":"q","http://www.baidu.com":"kw", "http://www.google.com":"lst-ib", "http://www.bing.com":"sb_form_q"}

	## Todo : measure time on mobile web view
	
	## Todo : measure time on mobile chrome
	# connect to mobile chrome using selenium