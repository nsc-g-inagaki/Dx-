import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup

f = open('scraped-seraku-services.csv', 'w')
writer = csv.writer(f, lineterminator='\n')

site = requests.get('https://www.seraku.co.jp/service/').text
soup = BeautifulSoup(site, 'html.parser')
section = soup.select("div" '.summary-p__name_jp')

csvlist = []
for dx_and_si in section:
    all_name = dx_and_si.text
    if 'Dx' in all_name:
       dx_si = dx_and_si.find('span', class_='dx_icon')
       service_name = all_name.strip('DX')
    elif 'SI' in all_name:
       dx_si = dx_and_si.find('span', class_='si_icon')
       service_name = all_name.strip('SI')
    csvlist.append([dx_si.text, service_name])

Column = ['サービス分野', 'サービス名']

df = pd.DataFrame(csvlist,columns=Column)

df.to_csv(r"scraped-seraku-services.csv",encoding='utf_8_sig')

