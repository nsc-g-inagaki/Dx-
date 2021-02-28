#ユーザー入力用
total = int(input("総数= "))
num = str(input("対象値= "))
list = num.split()

print(sorted(set(list))[-2])


input("処理終了")
