import math

#ユーザー入力用
print("任意の自然数を入力してください")
num_a = float(input("a= "))
num_b = float(input("b= "))

#割り算（小数点以下切り捨て)
print(math.floor(num_a / num_b))

#割り算（小数点込み）
print(num_a / num_b)

input("処理終了")
