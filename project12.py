import datetime
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

print('영원회귀: 블랙서바이벌의 티어 분포도(솔로 기준) \n')
webpage = urllib.request.urlopen('https://dak.gg/bser/statistics/tier')
soup = BeautifulSoup(webpage, 'html.parser')
tables = soup.select('table')
table = tables[0]
table_html = str(table)
table_df_list = pd.read_html(table_html)
table_df = table_df_list[0]
print(table_df)
list1 = table_df['Tier'].tolist()
list2 = table_df['Percentage'].tolist()
L=''.join(list2)
L2=L.split('%')
L2.remove('')

tier1 = []
for tier in list1:
    if "1" in tier:
        tier1.append(tier)
tier1 = [tier.strip("1") for tier in tier1]
tier1.insert(0,"Immortal")
tier1.insert(1,"Titan")
tier1.reverse()
TT1=0
for s in range(22,26):
    TT1+=float(L2[s])
TT2=0
for s in range(18,22):
    TT2+=float(L2[s])
TT3=0
for s in range(14,18):
    TT3+=float(L2[s])
TT4=0
for s in range(10,14):
    TT4+=float(L2[s])
TT5=0
for s in range(6,10):
    TT5+=float(L2[s])
TT6=0
for s in range(2,6):
    TT6+=float(L2[s])
tier_size = [TT1,TT2,TT3,TT4,TT5,TT6,float(L2[1]),float(L2[0])]

width_num = 0.4
plt.axis('equal')
plt.pie(tier_size, labels = tier1, autopct='%1.1f%%')
plt.title('영원회귀: 블랙서바이벌의 티어 분포 그래프(솔로 기준)', fontsize=30)
plt.show()