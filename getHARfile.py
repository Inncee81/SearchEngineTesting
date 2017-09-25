from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from browsermobproxy import Server
from haralyzer import HarPage

#urlDict = {'http://www.naver.com':'query', 'http://www.daum.net':'q', "http://www.baidu.com":"kw", "http://www.google.com":"lst-ib", "http://www.bing.com":"sb_form_q"}
urlDict = {'http://www.naver.com':'query'}
keyword = "충남대학교"

if __name__ == "__main__":
	for url in urlDict:
		urlName = url.split(".")[1]
		server = Server("browsermob-proxy-2.1.4/bin/browsermob-proxy") 
		server.start()
		proxy = server.create_proxy()

		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("--incognito")
		driver = webdriver.Chrome(chrome_options=chrome_options)
		
		driver.get(url)
		time.sleep(5)

		proxy.new_har(urlNmae+"_"+keyword)
		inputElement = driver.find_element_by_id(urlDict[url])
		inputElement.send_keys(keyword)
		time.sleep(3)
		inputElement.send_keys(Keys.RETURN)
		time.sleep(5)

		result = proxy.har
		print(result)


server.stop()
driver.quit()