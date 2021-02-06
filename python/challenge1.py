#問題1 PythonでHello World
def Q1():
    print("Hello, World!")

#問題2 条件分岐
def Q2(n):
    #nが奇数の場合、規格外
    if n % 2 == 1:
        print(n,"は規格外です。")
    #nが偶数で、2 <= n <= 5の場合、規格内
    elif n % 2 == 0 and n >= 2 and n <= 5:
        print(n,"は規格内です。")
    #nが偶数で、6 <= n <= 20の場合、規格外
    elif n % 2 == 0 and n >= 6 and n <= 20:
        print(n,"は規格外です。")
    #nが偶数で、20 < n の場合、規格内
    elif n % 2 == 0 and n > 20:
        print(n,"は規格内です。")
    #1<= n <= 100の場合、対象外
    elif n >= 1 and n <= 100:
        print(n,"は対象外です。")

#問題3 算術
def Q3(a, b):
    print("a + b =",a + b)
    print("a - b =",a - b)
    print("a * b =",a * b)

#問題4 割り算
def Q4(a, b):
    #切り捨て処理にはmathライブラリが必要
    import math
    print("a / b =",math.floor(a / b),"（小数点以下切り捨て）")
    print("a / b =",a / b,"（小数点以下も表示）")

#問題5 ループ
def Q5(n: int):
    #0～n-1までの整数をmに格納して繰り返し処理
    for m in range(n):
        print(m,"の","2乗=", m**2)
        m = m + 1
        #ループが100回以上の場合
        if m > 100:
            print("無限ループ防止のため強制終了します。")
            break

#問題6　うるう年
def Q6(n: int):
    #400年に一度はうるう年
    if n % 400 == 0:
        print(True)
    #上記以外で100年に一度はうるう年ではない
    elif n % 100 == 0:
        print(False)
    #上記以外で4年に一度はうるう年
    elif n % 4 == 0:
        print(True)
    #上記以外はうるう年ではない
    else:
        print(False)
    #calenderライブラリのisleap関数を使うのは反則でしょうか・・・？

#問題7 Print関数
def Q7(n: int):
    #range関数で連番を生成し、list関数で配列化、配列をprintして一度に表示
    print(list(range(1, n+1)))

#問題8 抽出
def Q8(text):
    #入力値を半角スペースで分割、配列に格納
    array = text.split(' ')
    #整数型に変換
    array = list(map(int, array))
    #配列の長さを表示
    print("入力値の総数：", len(array))
    #配列を降順に並べ替え
    array.sort(reverse=True)
    #配列の要素ごとにループ
    for n in array:
        #取得した要素が1番目の数字より小さくなった時点で2番目の数字を表示、ループを抜ける
        if n < array[0]:
            print("2番目の数字：", n)
            break
    #ループを最後まで実行し、1番目の数字より小さい数が無い場合は2番目の数字が無い
    if n == array[0]:
        print("2番目の数字はありません。")

#問題9 シャッフル
def Q9(text):
    #randomモジュールのshuffle関数を利用
    import random
    #入力値を半角スペースで分割、配列に格納
    array = text.split(' ')
    #配列をシャッフル
    random.shuffle(array)
    #シャッフルされた名前を半角スペース区切りで文字列結合して表示
    print(" ".join(array))
