import cv2

# 分類器ディレクトリ(以下から取得)
# https://github.com/opencv/opencv/tree/master/data/haarcascades

def img_proc(imgPath):

    face_cascade_path = './data/haarcascades/haarcascade_frontalface_default.xml'
    eye_cascade_path = './data/haarcascades/haarcascade_eye.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

    output_path = "./opencv_face_detect_rectangle.jpg"

    src = cv2.imread(imgPath) #画像の読み込み

    try: #例外処理
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY) #グレースケールに変換
    except:
        print("画像がみつかりません")
        exit()

    faces = face_cascade.detectMultiScale(src_gray)

    for x, y, w, h in faces:
        cv2.rectangle(src, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = src[y: y + h, x: x + w]
        face_gray = src_gray[y: y + h, x: x + w]
        eyes = eye_cascade.detectMultiScale(face_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    src = cv2.resize(src, (400, 400))
    cv2.rectangle(src, (110, 355), (300, 390), (255, 255, 255), -1)
    cv2.putText(src, 'Press Esc to Exit', (120, 380), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.imshow("image2", src)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()

    exit()