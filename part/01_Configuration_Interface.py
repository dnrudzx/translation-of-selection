import sys
from PyQt5.QtWidgets import *       #install pyqt5

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('화면 구성')
        self.setGeometry(100,100,230,70)

        btn_capture = QPushButton('캡쳐',self)
        btn_capture.move(20,20)

        btn_trans = QPushButton('번역',self)
        btn_trans.move(120,20)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())