
#対象値を入力
nums = input("対象値を入力").split()

#２番目に大きい数字を取得
second = sorted(set(nums))[-2]

#結果を出力
print(second)
