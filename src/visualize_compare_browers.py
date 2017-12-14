## Draw boxplot about Dom Loading Time
## Draw boxplot about 

import matplotlib.pyplot as plt
import pandas as pd

def visualizeTimeOn3Browsers(measurementData_c, measurementData_f, measurementData_i, typeOfTime):
	c_plt = [] # chrome measurement data
	f_plt = [] # firefox measurement data
	i_plt = [] # ie measurement data

	urlList = measurementData_c['url'].unique()
	urlList = urlList.tolist()
	#urlList.remove('http://www.bing.com')

	fig1 = plt.figure()
	ax1 = fig1.add_subplot(111)

	fig2 = plt.figure()
	ax2 = fig2.add_subplot(111)

	fig3 = plt.figure()
	ax3 = fig3.add_subplot(111)

	domainNameList = []

	for url in urlList:
		c_timeDataOnURL = measurementData_c[measurementData_c['url'] == url]
		pageLoadingTimeSeries = c_timeDataOnURL[typeOfTime]
		c_plt.append(pageLoadingTimeSeries)

		f_timeDataOnURL = measurementData_f[measurementData_f['url'] == url]
		pageLoadingTimeSeries = f_timeDataOnURL[typeOfTime]
		f_plt.append(pageLoadingTimeSeries)

		i_timeDataOnURL = measurementData_i[measurementData_i['url'] == url]
		pageLoadingTimeSeries = i_timeDataOnURL[typeOfTime]
		i_plt.append(pageLoadingTimeSeries)

		domainName = url.split('.')[1]
		domainNameList.append(domainName)

	maxValue = getMaxValue(measurementData_c, measurementData_f,measurementData_i, typeOfTime)
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
	fig1.savefig('../image/chrome_'+typeOfTime+'_Compare.png', bbox_inches='tight')

	ax2.boxplot(f_plt)
	ax2.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax2.set_xticklabels(domainNameList)
	fig2.savefig('../image/firefox_'+typeOfTime+'_Compare.png', bbox_inches='tight')

	ax3.boxplot(i_plt)
	ax3.set_ylim(ymin = 0, ymax = maxValue+buffer)
	ax3.set_xticklabels(domainNameList)
	fig3.savefig('../image/IE_'+typeOfTime+'_Compare.png', bbox_inches='tight')

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

if __name__ == "__main__":
	measurementData_c = pd.read_csv('../csv/P_C_searchTime_result_finedust.csv')
	measurementData_i = pd.read_csv('../csv/P_I_searchTime_result.csv')
	measurementData_f = pd.read_csv('../csv/P_F_searchTime_result_finedust.csv')

	visualizeTimeOn3Browsers(measurementData_c, measurementData_f, measurementData_i, 'searchTime')
	visualizeTimeOn3Browsers(measurementData_c, measurementData_f, measurementData_i, 'networkTime')
	visualizeTimeOn3Browsers(measurementData_c, measurementData_f, measurementData_i, 'domLoadTime')