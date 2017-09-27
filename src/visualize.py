## Draw boxplot about Dom Loading Time
## Draw boxplot about 

import matplotlib.pyplot as plt
import pandas as pd

####################################################################################################################
##	* visualizeSearchTime : 각 웹 사이트의 검색 시간 측정 결과를 시각화하여 비교
####################################################################################################################
def visualizeSearchTime(measurementData, browserName):
	## get unique url in measurementData
	urlList = measurementData['url'].unique()
	urlList = urlList.tolist()
	domainNameList = []
	searchTimeList = []


	fig = plt.figure()
	ax = fig.add_subplot(111)

	for url in urlList:
		## split measurementData by url
		timeDataOnURL = measurementData[measurementData['url'] == url]
		searchTimeSeries = timeDataOnURL['searchTime']
		searchTimeList.append(searchTimeSeries)

		domainName = url.split('.')[1]
		domainNameList.append(domainName)

	ax.boxplot(searchTimeList)
	ax.set_xticklabels(domainNameList)

	fig.savefig('../image/'+browserName+'_searchTimeCompare'+'_'+browserName+'.png', bbox_inches='tight')

####################################################################################################################
##	* visualizeNetworkTime : 각 웹 사이트의 네트워크 시간 측정 결과를 시각화하여 비교
####################################################################################################################
def visualizeNetworkTime(measurementData, browserName):
	## get unique url in measurementData
	urlList = measurementData['url'].unique()
	urlList = urlList.tolist()
	domainNameList = []
	networkTimeList = []


	fig = plt.figure()
	ax = fig.add_subplot(111)

	for url in urlList:
		## split measurementData by url
		timeDataOnURL = measurementData[measurementData['url'] == url]
		networkTimeSeries = timeDataOnURL['networkTime']
		networkTimeList.append(networkTimeSeries)

		domainName = url.split('.')[1]
		domainNameList.append(domainName)

	ax.boxplot(networkTimeList)
	ax.set_xticklabels(domainNameList)
	fig.savefig('../image/'+browserName+'_networkTimeCompare'+'_'+browserName+'.png', bbox_inches='tight')

####################################################################################################################
##	* visualizeDomLoadingTime : 각 웹 사이트의 DOM 로딩 시간 측정 결과를 시각화하여 비교
####################################################################################################################
def visualizeDomLoadingTime(measurementData, browserName):
	## get unique url in measurementData
	urlList = measurementData['url'].unique()
	urlList = urlList.tolist()
	domainNameList = []
	domLoadingTimeList = []

	fig = plt.figure()
	ax = fig.add_subplot(111)

	for url in urlList:
		## split measurementData by url
		timeDataOnURL = measurementData[measurementData['url'] == url]
		domLoadingTimeSeries = timeDataOnURL['domLoadTime']
		domLoadingTimeList.append(domLoadingTimeSeries)

		domainName = url.split('.')[1]
		domainNameList.append(domainName)

	ax.boxplot(domLoadingTimeList)
	ax.set_xticklabels(domainNameList)
	fig.savefig('../image/'+browserName+'_domLoadingTimeCompare.png', bbox_inches='tight')


####################################################################################################################
##	* visualizeDomLoadingTime : 각 웹 사이트의 DOM 로딩 시간 측정 결과를 시각화하여 비교
####################################################################################################################
def visualizePageLoadingTime(measurementData, browserName):
	## get unique url in measurementData
	urlList = measurementData['url'].unique()
	urlList = urlList.tolist()
	domainNameList = []
	pageLoadingTimeList = []

	fig = plt.figure()
	ax = fig.add_subplot(111)

	for url in urlList:
		## split measurementData by url
		timeDataOnURL = measurementData[measurementData['url'] == url]
		pageLoadingTimeSeries = timeDataOnURL['pageLoadTime']
		pageLoadingTimeList.append(pageLoadingTimeSeries)

		domainName = url.split('.')[1]
		domainNameList.append(domainName)

	ax.boxplot(pageLoadingTimeList)
	ax.set_xticklabels(domainNameList)
	fig.savefig('../image/'+browserName+'_pageLoadingTimeCompare.png', bbox_inches='tight')


if __name__=="__main__":
	## load data
	measurementData = pd.read_csv('../csv/P_C_searchTime_result.csv')
	
	browserName = "chrome"
	#visualizeSearchTime(measurementData, browserName)
	#visualizeNetworkTime(measurementData, browserName)
	#visualizeDomLoadingTime(measurementData, browserName)
	visualizePageLoadingTime(measurementData, browserName)

	measurementData = pd.read_csv('../csv/P_F_searchTime_result.csv')
	browserName = "Firefox"

	#visualizeSearchTime(measurementData, browserName)
	#visualizeNetworkTime(measurementData, browserName)
	#visualizeDomLoadingTime(measurementData, browserName)
	visualizePageLoadingTime(measurementData, browserName)
