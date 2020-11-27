import sys
from PyQt5.QtWidgets import *
from PIL import ImageGrab
import cv2
import io
import os
from google.cloud import vision
import requests

client_id = "[NAVER Client id]"
client_secret = "[NAVER Client Secret]"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./[Service_Account_Key].json"

img = None
x_start = None
y_start = None
Mouse_Down = False

def draw_selective_area(event, x, y, flags, param):
    global Mouse_Down, x_start, y_start
    if event == cv2.EVENT_LBUTTONDOWN:
        Mouse_Down = True
        x_start = x
        y_start = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if Mouse_Down:
            drawing_page = img.copy()
            cv2.rectangle(drawing_page, (x_start, y_start), (x, y), (0, 255, 0),2)
            cv2.imshow('img',drawing_page)
    elif event == cv2.EVENT_LBUTTONUP:
        if Mouse_Down:
            Lbtn_Down = False
            width = x - x_start
            height = y - y_start

            rect = [-1, -1, -1, -1]
            if height > 0:
                rect[0] = y_start
                rect[1] = y_start + height
            else:
                rect[0] = y
                rect[1] = y_start
            if width > 0:
                rect[2] = x_start
                rect[3] = x_start + width
            else:
                rect[2] = x
                rect[3] = x_start
            if width != 0 and height != 0:
                roi = img[rect[0]:rect[1], rect[2]:rect[3]]
                cv2.imshow('select_area', roi)
                cv2.moveWindow('select_area', 0, 0)
                cv2.imwrite('./select_area.png', roi)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('화면 구성')
        self.setGeometry(100,100,230,70)

        btn_capture = QPushButton('캡쳐',self)
        btn_capture.move(20,20)
        btn_capture.clicked.connect(self.capture)

        btn_trans = QPushButton('번역',self)
        btn_trans.move(120,20)
        btn_trans.clicked.connect(self.translate)

    def capture(self):
        global img
        capture_img = ImageGrab.grab().resize((900, 600))
        capture_img.save('capture.png')

        img = cv2.imread('./capture.png')
        cv2.imshow('img', img)
        cv2.setMouseCallback('img', draw_selective_area)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def translate(self):
        client = vision.ImageAnnotatorClient()
        file = os.path.abspath('select_area.png')
        with io.open(file, 'rb') as img:
            content = img.read()
        img = vision.Image(content=content)
        response = client.text_detection(image=img)
        texts = response.text_annotations
        text = format(texts[0].description)
        #print(format(texts[0].description))

        url = "https://openapi.naver.com/v1/papago/n2mt"
        headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
        params = {"source": "en", "target": "ko", "text": text}
        try:
            response = requests.post(url, headers=headers, data=params)
            result = response.json()
            print(result['message']['result']['translatedText'])
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())