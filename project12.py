import datetime
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

print('영원회귀: 블랙서바이벌의 티어 분포도 \n')
webpage=urllib.request.urlopen('https://dak.gg/bser/statistics/tier')
soup=BeautifulSoup(webpage,'html.parser')
tables = soup.select('table')
table = tables[0]
table_html = str(table)
table_df_list = pd.read_html(table_html)
table_df=table_df_list[0]
print(table_df)