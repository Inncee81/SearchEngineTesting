## Draw boxplot about Dom Loading Time
## Draw boxplot about 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.patches as mpatches
from matplotlib import font_manager, rc

####################################################################################################################
##	* visualizeSearchTime : 각 웹 사이트의 검색 시간 측정 결과를 시각화하여 비교
####################################################################################################################
def visualizeSearchTime_boxplot(measurementData, browserName, columnName, searchKeyword):
	## get unique url in measurementData
	urlList = measurementData['url'].unique()
	urlList = urlList.tolist()

	## remove baidu, yahoo jp
	urlList.remove('http://www.baidu.com')
	urlList.remove('http://www.yahoo.co.jp')
	domainNameList = []
	searchTimeList = []


	fig = plt.figure()
	ax = fig.add_subplot(111)

	for url in urlList:
		## split measurementData by url
		timeDataOnURL = measurementData[measurementData['url'] == url]
		searchTimeSeries = timeDataOnURL[columnName]
		searchTimeList.append(searchTimeSeries)

		domainName = url.split('.')[1]
		domainNameList.append(domainName)

	ax.boxplot(searchTimeList)
	ax.set_xticklabels(domainNameList)

	fig.savefig('../image/'+browserName+'_'+searchKeyword+'_'+columnName+'.png', bbox_inches='tight')

def splitDataByURL(measurementData, url):
	resultDF = measurementData.loc[measurementData['url'] == url]

	return resultDF


def visualizeSearchTime_stackedBarPlot(measurementData, browserName, searchKeyword):
	naverData = splitDataByURL(measurementData, "http://www.naver.com")
	daumData = splitDataByURL(measurementData, "http://www.daum.net")
	googleData = splitDataByURL(measurementData, "http://www.google.com")
	bingData = splitDataByURL(measurementData, "http://www.bing.com")
	baiduData = splitDataByURL(measurementData, "http://www.baidu.com")

	## Draw stackedBarPlot 
	##- bottom Bar : network Time - middle Bar value
	##- middle Bar : overlapped Time between network Time and page loading time, 
	##- top bar : Page loading time - middle Bar value,

	meanOfSTInNaver = naverData['searchTime'].mean()
	meanOfNTInNaver = naverData['networkTime'].mean()
	meanOfPTInNaver = naverData['pageLoadTime'].mean()
	overlappedTimeInNaver = meanOfNTInNaver+meanOfPTInNaver-meanOfSTInNaver

	meanOfSTInDaum = daumData['searchTime'].mean()
	meanOfNTInDaum = daumData['networkTime'].mean()
	meanOfPTInDaum = daumData['pageLoadTime'].mean()
	overlappedTimeInDaum = meanOfNTInDaum+meanOfPTInDaum-meanOfSTInDaum

	meanOfSTInGoogle = googleData['searchTime'].mean()
	meanOfNTInGoogle = googleData['networkTime'].mean()
	meanOfPTInGoogle = googleData['pageLoadTime'].mean()
	overlappedTimeInGoogle = meanOfNTInGoogle+meanOfPTInGoogle-meanOfSTInGoogle

	meanOfSTInBing = bingData['searchTime'].mean()
	meanOfNTInBing = bingData['networkTime'].mean()
	meanOfPTInBing = bingData['pageLoadTime'].mean()
	overlappedTimeInBing = meanOfNTInBing+meanOfPTInBing-meanOfSTInBing

	bottom_bar = [meanOfNTInNaver-overlappedTimeInNaver, meanOfNTInDaum-overlappedTimeInDaum, meanOfNTInGoogle-overlappedTimeInGoogle, meanOfNTInGoogle-overlappedTimeInBing]
	middle_bar = [overlappedTimeInNaver, overlappedTimeInDaum, overlappedTimeInGoogle, overlappedTimeInBing]
	top_bar = [meanOfPTInNaver-overlappedTimeInNaver, meanOfPTInDaum-overlappedTimeInDaum, meanOfPTInGoogle-overlappedTimeInGoogle, meanOfPTInBing-overlappedTimeInBing]

	font_name = font_manager.FontProperties(fname="C:\\Users\\miw52\\Documents\\malgun.ttf").get_name()
	rc('font', family=font_name)

	bm_data = []
	for i in range(0, len(bottom_bar)):
		bm_data.append(bottom_bar[i]+middle_bar[i])

	names = ['naver', 'daum', 'google', 'bing']
	r = [0,1,2,3]
	barwidth = 1

	plt.bar(r, bottom_bar,color='#2b3f6b', edgecolor='white', width=barwidth)
	plt.bar(r, middle_bar, bottom = bottom_bar, color='#7b8ea9', edgecolor='white', width=barwidth)
	plt.bar(r, top_bar, bottom = bm_data, color='#f89b6c', edgecolor='white', width=barwidth)

	plt.xticks(r, names, fontweight='bold')
	#plt.xlabel("Search Web Service")
	plt.xlabel("검색 웹 서비스")
	plt.ylabel("검색 시간(ms)")

	nt_patch = mpatches.Patch(color='#2b3f6b', label = "network Time - overlapped Time")
	overlap_patch = mpatches.Patch(color = '#7b8ea9', label = "overlapped Time")
	pt_patch = mpatches.Patch(color = '#f89b6c', label = "page loading Time - overlapped Time")

	plt.legend(handles=[pt_patch, overlap_patch, nt_patch], fontsize = 8)
	# Show graphic
	plt.savefig("../image/"+browserName+"_"+searchKeyword+"_stackedPlot.png")


def visualizeSearchTime_barPlot(measurementData, browserName, searchKeyword):
	font_name = font_manager.FontProperties(fname="C:\\Users\\miw52\\Documents\\malgun.ttf").get_name()
	rc('font', family=font_name)
	naverData = splitDataByURL(measurementData, "http://www.naver.com")
	daumData = splitDataByURL(measurementData, "http://www.daum.net")
	googleData = splitDataByURL(measurementData, "http://www.google.com")
	bingData = splitDataByURL(measurementData, "http://www.bing.com")
	baiduData = splitDataByURL(measurementData, "http://www.baidu.com")

	meanOfSTInNaver = naverData['searchTime'].mean()
	meanOfNTInNaver = naverData['networkTime'].mean()
	meanOfPTInNaver = naverData['pageLoadTime'].mean()
	overlappedTimeInNaver = meanOfNTInNaver+meanOfPTInNaver-meanOfSTInNaver

	meanOfSTInDaum = daumData['searchTime'].mean()
	meanOfNTInDaum = daumData['networkTime'].mean()
	meanOfPTInDaum = daumData['pageLoadTime'].mean()
	overlappedTimeInDaum = meanOfNTInDaum+meanOfPTInDaum-meanOfSTInDaum

	meanOfSTInGoogle = googleData['searchTime'].mean()
	meanOfNTInGoogle = googleData['networkTime'].mean()
	meanOfPTInGoogle = googleData['pageLoadTime'].mean()
	overlappedTimeInGoogle = meanOfNTInGoogle+meanOfPTInGoogle-meanOfSTInGoogle

	meanOfSTInBing = bingData['searchTime'].mean()
	meanOfNTInBing = bingData['networkTime'].mean()
	meanOfPTInBing = bingData['pageLoadTime'].mean()
	overlappedTimeInBing = meanOfNTInBing+meanOfPTInBing-meanOfSTInBing

	index = np.arange(4)
	bar_width = 0.3

	opacity = 0.3
	mNT = [meanOfNTInBing, meanOfNTInGoogle, meanOfNTInDaum, meanOfNTInNaver]
	emptyTime1 = [meanOfSTInBing-meanOfNTInBing,meanOfSTInGoogle-meanOfNTInGoogle, meanOfSTInDaum-meanOfNTInDaum,meanOfSTInNaver-meanOfNTInNaver]
	emptyTime2 = [meanOfSTInBing-meanOfPTInBing,meanOfSTInGoogle-meanOfPTInGoogle, meanOfSTInDaum-meanOfPTInDaum,meanOfSTInNaver-meanOfPTInNaver]
	mPT = [meanOfPTInBing, meanOfPTInGoogle, meanOfPTInDaum, meanOfPTInNaver]
	#mPT = ()
	#m
	bar1 = plt.barh(index, mNT, color = '#f89b6c', height = bar_width, edgecolor = "black")
	bar2 = plt.barh(index, emptyTime1,left = mNT, color= "white", height = bar_width, edgecolor = "black")
	bar3 = plt.barh(index-bar_width, emptyTime2,color ="white", height = bar_width, edgecolor = "black")
	bar4 = plt.barh(index-bar_width, mPT, left = emptyTime2, color = "#2b3f6b", height = bar_width, edgecolor = "black")

	plt.yticks(index-bar_width/2, ('bing', 'google', 'daum', 'naver'), fontweight='bold')
	plt.xlabel("검색 시간(ms)")
	plt.ylabel("검색 웹 서비스")

	nt_patch = mpatches.Patch(color = '#f89b6c',label = "네트워크 시간")
	pt_patch = mpatches.Patch(color = '#2b3f6b',label = "페이지 로딩 시간")
	plt.title("검색 서비스별 검색 시간 구성")
	plt.legend(handles=[nt_patch,pt_patch], fontsize = 8)
	plt.show()
	#plt.bar(index+bar_width, mNT,color='white', edgecolor='white', width=bar_width)
	#plt.bar(r, middle_bar, bottom = bottom_bar, color='#7b8ea9', edgecolor='white', width=bar_width)

if __name__=="__main__":
	## load data
	measurementData_c = pd.read_csv('../csv/P_C_searchTime_result_kiise.csv')
	
	browserName = "chrome"
	#visualizeSearchTime(measurementData_c, browserName, "searchTime", "정보과학회")
	#visualizeSearchTime(measurementData_c, browserName, "networkTime", "정보과학회")
	#visualizeSearchTime(measurementData_c, browserName, "pageLoadTime", "정보과학회")

	visualizeSearchTime_barPlot(measurementData_c, browserName, "정보과학회")