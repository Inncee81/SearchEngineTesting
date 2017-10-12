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

	for i in range(0, len(pageLoadingTimeList)):
		print(pageLoadingTimeList[i])
		print("---------------------------------------")

	ax.boxplot(pageLoadingTimeList)
	ax.set_xticklabels(domainNameList)
	fig.savefig('../image/'+browserName+'_pageLoadingTimeCompare.png', bbox_inches='tight')

def visualizeSearchTimeOn3Browsers(measurementData_c, measurementData_f, measurementData_i):
	c_plt = [] # chrome measurement data
	f_plt = [] # firefox measurement data
	i_plt = []

	urlList = measurementData_c['url'].unique()
	urlList = urlList.tolist()
	urlList.remove('http://www.bing.com')

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)

	fig2 = plt.figure()
	ax2 = fig2.add_subplot(111)

	fig3 = plt.figure()
	ax3 = fig3.add_subplot(111)

	domainNameList = []

	for url in urlList:
		c_timeDataOnURL = measurementData_c[measurementData_c['url'] == url]
		pageLoadingTimeSeries = c_timeDataOnURL['searchTime']
		c_plt.append(pageLoadingTimeSeries)

		f_timeDataOnURL = measurementData_f[measurementData_f['url'] == url]
		pageLoadingTimeSeries = f_timeDataOnURL['searchTime']
		f_plt.append(pageLoadingTimeSeries)

		i_timeDataOnURL = measurementData_i[measurementData_i['url'] == url]
		pageLoadingTimeSeries = i_timeDataOnURL['searchTime']
		i_plt.append(pageLoadingTimeSeries)

		domainName = url.split('.')[1]
		domainNameList.append(domainName)

	maxValue = getMaxValue(measurementData_c, measurementData_f, 'searchTime')
	buffer = 0

	if maxValue > 1000:
		buffer = 1000
	elif maxValue < 1000 and maxValue > 100:
		buffer = 100
	elif maxValue < 100 and maxValue > 10:
		buffer = 10
	elif maxValue < 10:
		buffer = 5
	
	ax1.boxplot(c_plt)
	ax1.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax1.set_xticklabels(domainNameList)
	fig1.savefig('../image/chrome_searchTimeCompare.png', bbox_inches='tight')

	ax2.boxplot(f_plt)
	ax2.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax2.set_xticklabels(domainNameList)
	fig2.savefig('../image/firefox_searchTimeCompare.png', bbox_inches='tight')

	ax3.boxplot(i_plt)
	ax3.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax3.set_xticklabels(domainNameList)
	fig3.savefig('../image/IE_searchTimeCompare.png', bbox_inches='tight')

def visualizeNetworkTimeOn3Browsers(measurementData_c, measurementData_f, measurementData_i):
	c_plt = [] # chrome measurement data
	f_plt = [] # firefox measurement data
	i_plt = []

	urlList = measurementData_c['url'].unique()
	urlList = urlList.tolist()
	urlList.remove('http://www.bing.com')

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)

	fig2 = plt.figure()
	ax2 = fig2.add_subplot(111)

	fig3 = plt.figure()
	ax3 = fig3.add_subplot(111)

	domainNameList = []

	for url in urlList:
		c_timeDataOnURL = measurementData_c[measurementData_c['url'] == url]
		pageLoadingTimeSeries = c_timeDataOnURL['networkTime']
		c_plt.append(pageLoadingTimeSeries)

		f_timeDataOnURL = measurementData_f[measurementData_f['url'] == url]
		pageLoadingTimeSeries = f_timeDataOnURL['networkTime']
		f_plt.append(pageLoadingTimeSeries)

		i_timeDataOnURL = measurementData_i[measurementData_i['url'] == url]
		pageLoadingTimeSeries = i_timeDataOnURL['networkTime']
		i_plt.append(pageLoadingTimeSeries)

		domainName = url.split('.')[1]
		domainNameList.append(domainName)

	maxValue = getMaxValue(measurementData_c, measurementData_f, 'networkTime')
	buffer = 0

	if maxValue > 1000:
		buffer = 1000
	elif maxValue < 1000 and maxValue > 100:
		buffer = 100
	elif maxValue < 100 and maxValue > 10:
		buffer = 10
	elif maxValue < 10:
		buffer = 5
	
	ax1.boxplot(c_plt)
	ax1.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax1.set_xticklabels(domainNameList)
	fig1.savefig('../image/chrome_networkTimeCompare.png', bbox_inches='tight')

	ax2.boxplot(f_plt)
	ax2.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax2.set_xticklabels(domainNameList)
	fig2.savefig('../image/firefox_networkTimeCompare.png', bbox_inches='tight')

	ax3.boxplot(i_plt)
	ax3.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax3.set_xticklabels(domainNameList)
	fig3.savefig('../image/IE_networkTimeCompare.png', bbox_inches='tight')

def visualizeDomLoadingTimeOn3Browsers(measurementData_c, measurementData_f, measurementData_i):
	c_plt = [] # chrome measurement data
	f_plt = [] # firefox measurement data
	i_plt = []

	urlList = measurementData_c['url'].unique()
	urlList = urlList.tolist()
	urlList.remove('http://www.bing.com')

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)

	fig2 = plt.figure()
	ax2 = fig2.add_subplot(111)

	fig3 = plt.figure()
	ax3 = fig3.add_subplot(111)

	domainNameList = []

	for url in urlList:
		c_timeDataOnURL = measurementData_c[measurementData_c['url'] == url]
		pageLoadingTimeSeries = c_timeDataOnURL['domLoadTime']
		c_plt.append(pageLoadingTimeSeries)

		f_timeDataOnURL = measurementData_f[measurementData_f['url'] == url]
		pageLoadingTimeSeries = f_timeDataOnURL['domLoadTime']
		f_plt.append(pageLoadingTimeSeries)

		i_timeDataOnURL = measurementData_i[measurementData_i['url'] == url]
		pageLoadingTimeSeries = i_timeDataOnURL['domLoadTime']
		i_plt.append(pageLoadingTimeSeries)

		domainName = url.split('.')[1]
		domainNameList.append(domainName)

	maxValue = getMaxValue(measurementData_c, measurementData_f, 'domLoadTime')
	buffer = 0

	if maxValue > 1000:
		buffer = 1000
	elif maxValue < 1000 and maxValue > 100:
		buffer = 100
	elif maxValue < 100 and maxValue > 10:
		buffer = 10
	elif maxValue < 10:
		buffer = 5
	
	ax1.boxplot(c_plt)
	ax1.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax1.set_xticklabels(domainNameList)
	fig1.savefig('../image/chrome_domLoadTimeCompare.png', bbox_inches='tight')

	ax2.boxplot(f_plt)
	ax2.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax2.set_xticklabels(domainNameList)
	fig2.savefig('../image/firefox_domLoadTimeCompare.png', bbox_inches='tight')

	ax3.boxplot(i_plt)
	ax3.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax3.set_xticklabels(domainNameList)
	fig3.savefig('../image/IE_domLoadTimeCompare.png', bbox_inches='tight')


def getMaxValue(measurementData_c, measurementData_f, measurementData_i, columnName):
	c_maxSeries = measurementData_c.max(numeric_only = True)
	f_maxSeries = measurementData_f.max(numeric_only = True)
	i_maxSeries = measurementData_f.max(numeric_only = True)

	maxList = [c_maxSeries[columnName],f_maxSeries[columnName],i_maxSeries[columnName]]

	#maxValue = c_maxSeries[columnName]

	#if f_maxSeries[columnName] > maxValue:
	#	maxValue = f_maxSeries[columnName]

	#return maxValue
	return max(maxList)



if __name__=="__main__":
	## load data
	measurementData_c = pd.read_csv('../csv/P_C_searchTime_result.csv')
	
	browserName = "chrome"
	#visualizeSearchTime(measurementData, browserName)
	#visualizeNetworkTime(measurementData, browserName)
	#visualizeDomLoadingTime(measurementData, browserName)
	#visualizePageLoadingTime(measurementData, browserName)

	measurementData_f = pd.read_csv('../csv/P_F_searchTime_result.csv')
	browserName = "Firefox"

	#visualizeSearchTime(measurementData, browserName)
	#visualizeNetworkTime(measurementData, browserName)
	#visualizeDomLoadingTime(measurementData, browserName)
	#visualizePageLoadingTime(measurementData, browserName)

	visualizeSearchTimeOn3Browsers(measurementData_c, measurementData_f)
	#getMaxValue(measurementData_c, measurementData_f, 'searchTime')