import random

#ユーザー入力用
name = str(input("対象値= "))
list = name.split()

#リストシャッフル
random.shuffle(list)

#リスト要素数の数だけ繰り返し
for count in range(len(list)):
    #最終回以外
    if int(count) != len(list)-1:
        print(list[count],end =" ")
    else:
        print(list[count])

input("処理終了")
