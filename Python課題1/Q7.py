#ユーザー入力用
print("任意の自然数を入力してください")
num = int(input("--> "))

for count in range(1,num+1):
    print(count,end="")

input("処理終了")
