#ユーザー入力用
print("任意の自然数を入力してください")
num = int(input("--> "))

#入力値の回数分繰り返し（countは０からスタート）
for count in range(num):
    #countが０の時
    if count == 0:
        print(count)
        continue
    #countが０以降の時
    else:
        print(count ** 2)

input("処理終了")
