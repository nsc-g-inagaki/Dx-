# Python課題2

## 概要

次の条件に従い、顔認証を行うプログラムを作成してください。

### 条件

- OpenCVライブラリを使用する
- 対象画像はプログラム実行時にパラメーターとして1枚指定する
- 対象画像が見つからない場合は、その旨を表示してプログラムを終了する
- 認識した顔の周りに青い四角表示する
- 認識した目の周りに緑色の四角表示する
- 処理を施した画像を表示する際に、画面の下部に「Press Esc to Exit」と表示する
- 処理を施した画像の表示後、Escキーが押されたら画面を閉じる処理を行う
- 元の画像は、プログラム実行後編集されていないこと



def face(filename):
    import cv2
    import numpy as np
    
    #カスケード分類器を作成
    face_cascade_path = "haarcascade_frontalface_default.xml"
    eye_cascade_path = "haarcascade_eye.xml"
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
    
    #画像の読み込み
    img = cv2.imread(filename, 1)
    
    if img is None:
        #画像の読み込みに失敗した場合
        print("対象の画像が見つかりませんでした。プログラムを終了します。")
    else:
        #画像の読み込みに成功した場合
        print("画像の読み込みに成功しました。")
        
        #グレースケールに変換
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #顔を囲む色を指定
        face_rect_color = (255, 0, 0)
        #目を囲む色を指定
        eye_rect_color = (0, 255, 0)
        #顔を検出
        faces = face_cascade.detectMultiScale(img_gray)
        
        #検出された顔ごとに処理
        for (x,y,w,h) in faces:
            #顔と認識された領域を四角で囲む
            frame = cv2.rectangle(img, (x, y), (x + w, y + h), face_rect_color, 2)
            #顔領域を設定
            roi = frame[y:y + h, x:x + w]
            roi_gray = img_gray[y:y + h, x:x + w]
            #目を検出
            eyes = eye_cascade.detectMultiScale(roi_gray)
            #検出された目ごとに処理
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi, (ex, ey),(ex + ew, ey + eh),eye_rect_color, 2)
        
        #画像サイズを取得
        height, width, channels = img.shape[:3]
        #画像に文字を表示
        cv2.putText(img, "Press Esc to Exit",(0, height-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        
        #画像を表示
        cv2.imshow("Loaded Image",img)
        
        #ESCキーを押した場合
        key = cv2.waitKey(0) & 0xFF
        if key == 27:
            #ウィンドウを閉じる
            cv2.destroyAllWindows()
        
