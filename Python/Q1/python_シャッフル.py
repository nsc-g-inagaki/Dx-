import random

name = input('名前を入力(苗字と名前の間を半角スペースで区切ります)：').split()

random.seed(1)
random.shuffle(name)
print(*name)

input()