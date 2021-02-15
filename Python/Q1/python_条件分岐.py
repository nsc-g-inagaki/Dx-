n = int(input('数値を入力：'))

if n % 2 == 1:
   print('規格外')
elif 2 <= n <= 5:
   print('規格内')
elif 6 <= n <= 20:
   print('規格外')
elif n > 20:
   print('規格内')
elif 1 <= n <= 100:
   print('対象外')

input()