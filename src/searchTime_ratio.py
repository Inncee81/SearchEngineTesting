import pandas as pd

def getTimeRatio(_measurementData):
	urlList = measurementData['url'].unique()
	urlList = urlList.tolist()

	for url in urlList:
		print("* "+url+" *--------------------------------------------------------------")
		measurementDataOnURL = _measurementData.loc[_measurementData['url'] == url]
		meanOfST = measurementDataOnURL['searchTime'].mean()
		meanOfNT = measurementDataOnURL['networkTime'].mean()
		meanOfPT = measurementDataOnURL['pageLoadTime'].mean()
		overlappedTime = meanOfNT+meanOfPT-meanOfST

		print("- 네트워크 시간 비율 : ", meanOfNT/meanOfST*100)
		print("- 페이지 로딩 시간 비율 : ", meanOfPT/meanOfST*100)
		print("- 겹치는 시간 비율 : ", overlappedTime/meanOfST*100)


if __name__ == "__main__":
	measurementData = pd.read_csv("../csv/P_C_searchTime_result_kiise.csv")
	getTimeRatio(measurementData)