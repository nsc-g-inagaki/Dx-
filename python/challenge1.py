#1
def fn1():
    print("Hello, World!")

#2
def fn2(n):
    hoge = n % 2
    if hoge == 0:
        print("規格外")
    elif 2 <= n <= 5:
        print("規格内")
    elif 6 <= n <= 20:
        print("規格外")
    elif n < 20:
        print("規格内")
    elif 1 <= n <= 100:
        print("対象外")

#3
def fn3(a,b):
    print(a + b)
    print(a - b)
    print(a * b)

#4
def fn4(a,b):
    print(a // b)
    print(a / b)

#5
def fn5(n):
    for i in range(n):
        print(i ** 2)

#6
def fn6(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                print("true")
            else:
                print("false")
        else:
            print("true")
    else:
        print("false")

#7
def fn7(n):
    r = range(1, n+1)
    print(*list(r), sep="")

#8
def fn8(n, s):
    arr = set(s.split())
    print(sorted(arr)[-2])

#9
def fn9(s):
    import random
    ori = rdm = s.split()
    while ori == rdm:
        rdm = random.sample(rdm,len(rdm))
    print(*rdm)
