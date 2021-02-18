# Python課題3
#「セラクのサービス」](https://www.seraku.co.jp/service/)ページよりデータを抽出し、加工してください。
### 条件
#- サービス名　○
#- サービス分野（Dx又はSIのどちらか）　○
#- 抽出したデータをCSVファイルとして保存する　○
#- 保存するファイル名は「scraped-seraku-services.csv」とする　○
#- CSVファイルの保存場所は、このPythonプログラムと同じフォルダとする　○
#- 保存先に同じファイルが存在する場合は、上書き保存すること　○
#- CSVファイルの1行目はヘッダー行とする　○
#- ヘッダーは、「サービス分野, サービス名」とする　○
#- CSVファイルのエンコーディングはUTF-8であること ○

import csv
import requests
import bs4
from bs4 import BeautifulSoup

#ヘッダー
HEADER = ['サービス分野', 'サービス名']

#対象URLから情報を取得
url = 'https://www.seraku.co.jp/service/'
html = requests.get(url)

#htmlのテキスト情報のみを使用
soup = BeautifulSoup(html.text, 'html.parser')
seraku = soup.find_all(class_='heightbox-inner')
dx = soup.find_all(id='dx')
si = soup.find_all(id='si')

list1 = ['#agr', '#iot', '#data', '#rpa', '#sec', '#bui']
list2 = ['#iti', '#dig', '#web', '#loc']

#CSV出力
with open('scraped-seraku-services.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(HEADER)


    def dx_list(a):

        for d in dx:
            servicefield = d.find(class_='icon').text

            for l in list1:
                servicename = d.find(href= str(l)).text

                row = [servicefield, servicename]
                writer.writerow(row)

    def si_list(b):

        for s in si:
            servicefield = s.find(class_='icon').text

            for l in list2:
                servicename = s.find(href= str(l)).text

                row = [servicefield, servicename]
                writer.writerow(row)

    dx_list(dx)
    si_list(si)
