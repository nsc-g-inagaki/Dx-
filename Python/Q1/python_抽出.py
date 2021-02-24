n = int(input('総数を入力：'))
L = [int(i) for i in input('スペース区切りで数値を入力：').split()]

if len(L) == n:
   print(*L)
   print(sorted(set(L))[-2])
   input()
   exit()
else:
   print('入力した数値は総数と合いません')

print(*L)
input()