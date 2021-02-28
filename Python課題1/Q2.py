#ユーザー入力用
print("任意の自然数を入力してください")
num = int(input("--> "))

#入力値判定
#１より小さい場合
if num < 1:
    print("１より小さいため対象外")
else:
    #2で割ったあまりが1の場合(奇数)
    if num%2 == 1:
        print("奇数のため規格外")
    else:
        #2以上5以下の場合
        if num >= 2 and  num <=5:
            print("規格内")
        #6以上20以下の場合
        elif num >= 6 and num <= 20:
            print("6-20は規格外")
        #それ以外の場合
        else:
            print("規格内")

input("処理終了")
