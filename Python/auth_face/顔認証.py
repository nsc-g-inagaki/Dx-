import cv2
import numpy as np
import os, tkinter, tkinter.filedialog, tkinter.messagebox

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
tkinter.messagebox.showinfo('顔認証プログラム','画像ファイルを選択してください！')
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

# 処理ファイル名の出力
#tkinter.messagebox.showinfo('顔認証プログラム',file)

#拡張子の取得
filename, ext = os.path.splitext(file)

if ext != '.jpg' and ext != '.png' and ext != '.webp':
   tkinter.messagebox.showinfo('顔認証プログラム','選択したファイルは画像ファイルではありません。プログラムを終了します。')
   exit()

face_cascade_path = "C:\\Users\\m-aoki\\Desktop\\Python\\auth_face\\haarcascades\\haarcascade_frontalface_default.xml"
eye_cascade_path = "C:\\Users\\m-aoki\\Desktop\\Python\\auth_face\\haarcascades\\haarcascade_eye.xml"
output_path = "C:\\Users\\m-aoki\\Desktop\\Python\\auth_face\\trimmed\\new001.jpg"

face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

src = cv2.imread(file)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(src_gray, 1.3)

for x, y, w, h in faces:
    cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
    face = src[y: y + h, x: x + w]
    face_gray = src_gray[y: y + h, x: x + w]
    eyes = eye_cascade.detectMultiScale(face_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

#---------------------------------
message = "Press Esc to Exit"

height = src.shape[0]
width = src.shape[1]
print(width)
#フォントを作成
font = cv2.FONT_HERSHEY_SIMPLEX

w = cv2.getTextSize(message, font, 0.5, 1)[0]

#文字を書き込み。位置(左下を基準)、フォント、文字の大きさ、色、文字の太さ、線の種類)
cv2.putText(src, message, (width - int(w[0]), height - 5 ), font, 0.5, (0, 0, 255), 1, 16)
#---------------------------------


cv2.imwrite(output_path, src)

cv2.imshow('face_file', src)
cv2.waitKey()
