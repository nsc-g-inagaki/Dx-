def q1():
  print('Hello, World!')

def q2(n):
  
  if n%2 != 0:
    print('規格外')
  elif 2 <= n <= 5:
    print('規格内')
  elif 6 <= n <= 20:
    print('規格外')
  elif 20 < n:
    print('規格内')
  elif 1<= n <= 100:
    print('対象外')

def q3(a,b):
  print(a+b)
  print(a-b)
  print(a*b)

def q4(a,b):
  print(a//b)
  print(a/b)

def q5(n):
  for i in range(n):
    print(i**2)

def q6(y):
  if y%4 ==0 and (y%100 != 0 or y%400 == 0):
    print("True")
  else:
    print('False')

def q7(n):
  l = list(range(1,1+n))
  print(*l,sep='')

def q8():
  q8a(int(input('総数=')),[int(e) for e in input('対象値=').split()])

def q8a(l,n):
  if l == len(n):
    print(sorted(set(n))[-2])
  else:
    print('入力値が正しくありません')

def q9():
  q9a(input('名前の入力').split())

def q9a(name):
  import random
  random.shuffle(name)
  print(*name)