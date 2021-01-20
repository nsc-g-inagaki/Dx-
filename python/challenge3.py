#python 課題３

import requests
from bs4 import BeautifulSoup
import csv

filename = 'scraped-seraku-services.csv'

site = requests.get('https://www.seraku.co.jp/service/')
data = BeautifulSoup(site.text, 'html.parser')

service_div = [n.get_text() for n in data.select('.summary-p__name_jp span')]
service_name = [n.get_text() for n in data.select('div.summary-p__name_jp')]

# ファイル，1行目(カラム)の作成
with open(filename, 'w', newline="", encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(['サービス分野','サービス名'])

i = 0
for num in service_div:
    with open(filename, 'a', newline="", encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerow([service_div[i], service_name[i]])
        i += 1