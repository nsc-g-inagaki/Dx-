year = int(input('西暦を入力：'))

if year % 4 == 0:
   if year % 100 == 0:
      if year % 400 == 0:
         print(str(True))
      else:
         print(str(False))
   else:
      print(str(False))
else:
   print(str(False))

input()