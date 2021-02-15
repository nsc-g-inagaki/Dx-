import cv2
import numpy as np
import sys

img = cv2.imread(input('画像を指定してください：')) #画像を取り込み

if  type(img) is type(None):
	print('画像の指定が正しくありません')
	sys.exit()
else:
	face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	eye_cas = cv2.CascadeClassifier('haarcascade_eye.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #グレースケール化


face = face_cas.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7, minSize=(20, 20)) #顔認証の実行


for (x, y, w, h) in face: #顔を囲む
	cv2.rectangle(img, (x,y), (x + w, y + h),(255,0,0),3)
	roi_gray = gray[y: y + h, x: x + w]
	roi_color = img[y: y + h, x: x + w]
	
	eyes = eye_cas.detectMultiScale(roi_gray) #目認証の実行
	for (ex, ey, ew, eh) in eyes: #目を囲む
		cv2.rectangle(roi_color,(ex,ey),(ex + ew,ey + eh),(0,255,0),2)

cv2.putText(img,'Press Esc to Exit', (100,500) , cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 3, cv2.LINE_AA ) 

while True: #結果の表示
	cv2.imshow('img',img)
	k = cv2.waitKey(0)
	if k == 27:
		break

cv2.destroyAllWindows()




