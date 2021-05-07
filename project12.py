import datetime
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

print('블랙서바이벌 영원회귀의 티어 분포표 \n')
webpage = urllib.request.urlopen('https://dak.gg/bser/statistics/tier')
soup = BeautifulSoup(webpage, 'html.parser')
tables = soup.select('table')
table = tables[0]
table_html = str(table)
table_df_list = pd.read_html(table_html)
table_df = table_df_list[0]
list1 = table_df['Tier'].tolist()
list2 = table_df['Percentage'].tolist()
L=''.join(list2)
L2=L.split('%')
L2.remove('')
plt.pie(L2,labels=list1,autopct='%1.1f%%')

tier1 = []
for tier in list1:
    if "1" in tier:
        tier1.append(tier)
tier1 = [tier.strip("1") for tier in tier1]
tier1.insert(0,"Immortal")
tier1.insert(1,"Titan")
tier_size = [4.143, 38.61, 35.617, 13.939, 5.7, 1.283, 0.246, 0.167]

width_num = 0.4
fig, ax = plt.subplots()
ax.axis('equal')
pie_outside, _ = ax.pie(tier_size, radius = 1.3, labels = tier1, labeldistance = 0.8)
plt.setp(pie_outside, width = width_num, edgecolor = 'white')
pie_inside, plt_labels, junk = \
ax.pie(L2, radius=(1.3 - width_num), labels=list1, labeldistance=0.75, autopct='%1.1f%%')
plt.setp(pie_inside, width=width_num, edgecolor='white')
plt.title('블랙서바이벌 영원회귀의 티어 분포표', fontsize=30)
plt.show()
