num = input('西暦を入力_')

num = int(num)
print(num %400 == 0 or (num %4 == 0 and num %100 != 0 ))

