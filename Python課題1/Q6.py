#ユーザー入力用
print("うるう年か調べる年を入力してください")
num = int(input("--> "))

#4で割り切れない場合
if num%4 != 0:
    print("false")
else:
    #100で割り切れる場合
    if num%100 == 0:
        #かつ400でも割り切れる場合
        if num%400 == 0:
            print("true")
        #400では割り切れない場合
        else:
            print("false")
    else:
        print("false")

input("処理終了")
