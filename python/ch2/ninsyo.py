#Python課題2
    #OpenCVライブラリを使用する　○
    #対象画像はプログラム実行時にパラメーターとして1枚指定する　○
    #対象画像が見つからない場合は、その旨を表示してプログラムを終了する　○
    #認識した顔の周りに青い四角表示する　○
    #認識した目の周りに緑色の四角表示する　○
    #処理を施した画像を表示する際に、画面の下部に「Press Esc to Exit」と表示する ○
    #処理を施した画像の表示後、Escキーが押されたら画面を閉じる処理を行う　○
    #元の画像は、プログラム実行後編集されていないこと　○

import cv2
import sys
import glob
import pathlib
import tkinter
import os

# 分類器ディレクトリ
# https://github.com/opencv/opencv/blob/master/data/haarcascades/

cascade_path_face = './models/haarcascade_frontalface_default.xml'
cascade_path_eye = './models/haarcascade_eye.xml'


#画像パス
ImageFileName_path = pathlib.Path('./').glob('*.jpg')


for p in ImageFileName_path:

    Name = os.path.splitext(os.path.basename(p))[0]


    if os.path.exists(p):

    #対象画像はプログラム実行時にパラメーターとして1枚指定する　★
    #ファイル読み込み
        image = cv2.imread(p.name)

    #グレースケール変換
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #カスケード分類器の特徴量を取得する
        cascade_face = cv2.CascadeClassifier(cascade_path_face)
        cascade_eye = cv2.CascadeClassifier(cascade_path_eye)

    #顔検出実行
        facerect = cascade_face.detectMultiScale(image_gray)

        for x, y, w, h in facerect:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = image[y: y + h, x: x + w]
            face_gray = image_gray[y: y + h, x: x + w]
            eyes = cascade_eye.detectMultiScale(face_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    #認識結果の保存

        cv2.imwrite(Name + '_output.jpg',image)

    #画像読み込み（image2 = *_output.jpg）

        image2 = cv2.imread(Name + '_output.jpg')

    #認識画像リサイズ(image2 >>> image3)

        image3 = cv2.resize(image2, (250, 370))

    #リサイズ結果の保存

        cv2.imwrite(Name + '_resize.jpg', image3)

    #処理を施した画像を表示する際に、画面の下部に「Press Esc to Exit」と表示する

    #画像にテキストを表示する関数作成

        def write_text(outputimage_path):

            image4 = cv2.imread(Name + '_resize.jpg')

            cv2.putText(image4, 'Press Esc to Exit', (0, 365),
                    cv2.FONT_HERSHEY_PLAIN, 1.5,
                    (255, 0, 0), 1, cv2.LINE_AA)
            cv2.imwrite(Name + '_output_.jpg', image4)

    #画像作成関数の処理を実行
        write_text(Name + '_output.jpg')

    #処理後の画像表示

        image5 = cv2.imread(Name + '_output_.jpg')
        cv2.imshow(Name + '_output_.jpg',image5)
        k = cv2.waitKey(0)
        if k == 27:
            cv2.destroyAllWindows()

    #不要な画像削除
        os.remove(Name + '_resize.jpg')
        os.remove(Name + '_output.jpg')
        os.remove(Name + '_output_.jpg')

    sys.exit(0)

else:
    print("対象の画像が見つかりません。プログラムを終了します。")
    sys.exit(0)
