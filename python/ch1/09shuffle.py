# randomモジュールをインポート
import random

# 氏名を入力（listを定義）
name = input("氏名を入力").split()

#入力した氏名をシャッフル
shufflename = random.sample(name, len(name))

#結果を出力
print(' '.join(shufflename))
