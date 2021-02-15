import urllib.request
from bs4 import BeautifulSoup
import csv
# データ取得
req = urllib.request.urlopen('https://www.seraku.co.jp/service/')

soup = BeautifulSoup(req,"html.parser")

seraku_list = []

# データ加工
dxlist = soup.select('div#dx > li')
dx = soup.select('div#dx > .icon')

silist = soup.select('div#si > li')
si = soup.select('div#si > .icon')

for i in dxlist:
  seraku_list.append([dx[0].text + ',' + i.text])

for i in silist:
  seraku_list.append([si[0].text + ',' + i.text])

# csvファイル作成
with open('./scraped-seraku-services.csv','w',encoding='utf_8_sig') as f:
	fieldnames = ['サービス分野, サービス名']
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()

	writer = csv.writer(f)
	writer.writerows(seraku_list)
	



