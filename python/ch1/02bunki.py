a = int(input("値を入力"))

def bunki(n):
    if n % 2 == 0 and 2 <= n <= 5:
        print('規格内')
    elif n % 2 == 0 and 6 <= n <= 20:
        print('規格外')
    elif n % 2 == 0 and 20 < n:
        print('規格内')
    elif 1<= n <= 100:
        print('対象外')
    else:
        print('規格外')

bunki(a)
