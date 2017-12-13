import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.patches as mpatches
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname="C:\\Users\\miw52\\Documents\\malgun.ttf").get_name()
rc('font', family=font_name)

optData = pd.read_csv('../csv/samplePageLoadTest_optimized.csv')
data = pd.read_csv('../csv/samplePageLoadTest.csv')

optPLT = optData['plt']
originalPLT = data['plt']

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.boxplot([originalPLT, optPLT])
ax1.set_xticklabels(["original Data", "optimized Data"])
ax1.ylabel("페이지 로딩 시간(ms)")
ax1.title("미사용 컨텐츠 여부에 따른 페이지 로딩 시간 비교")
fig1.savefig('../image/aaa.png', bbox_inches='tight')