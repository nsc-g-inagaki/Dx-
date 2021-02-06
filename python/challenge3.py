def scraping():
    #Beautifulsoup4、Requests、CSVライブラリをインポート
    from bs4 import BeautifulSoup
    import requests
    import csv
    
    #取得対象URL
    target_url = 'https://www.seraku.co.jp/service/'
    #ページを取得
    r = requests.get(target_url)
    #ページを解析
    soup = BeautifulSoup(r.text, 'html.parser')
    #サービス一覧の2次元配列を作成し、ヘッダ行を追加
    seraku_serv = [['サービス分野','サービス名']]
    #DXとSIのリストを作る
    serv_div = ['dx','si']
    #DX、SIごとに処理を実行
    for div in serv_div:
        #対象サービス分野のaタグのテキスト（サービス名）を取得
        serv_list = [tag.text for tag in soup.find('div', id=div).find_all('a')]
        #取得したサービス名ごとに処理を実行
        for serv in serv_list:
            #サービス分野（大文字化）とサービス名を2次元配列に追加
            seraku_serv.append([div.upper(), serv])
    #CSVファイルを上書き、UTF-8（BOM付）オプションで開き、2次元配列をCSVファイルに書き込む
    with open('./scraped-seraku-services.csv', 'w', encoding="utf_8_sig") as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(seraku_serv)