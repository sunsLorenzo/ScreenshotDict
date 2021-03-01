import os
import time
import ocr
import baidutrans
import sys
imname = '/home/sun/Documents/APPs/screenshot_dict/abc.png'
os.system('deepin-screenshot -s /home/sun/Documents/APPs/screenshot_dict/abc.png')
# os.system(' python ocr.py')
words= ocr.get_words()
print(words,'-------')

##################### baidu trans API   ##################

# trans = baidutrans.trans(words)
# trans = trans['trans_result'][0]['dst']
# print(trans)

#####################    google API   #####################
import googletrans
trans = googletrans.trans_ch(words)


#####################   加上QT显示界面  #####################


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class TransApp(QWidget):
    def __init__(self):
        super().__init__()
        self.txt = QTextEdit(words)
        self.txt.setFont(QFont("Timers",10))
        self.trans_button = QPushButton(' Translate !!! click or press Ctrl')

        self.tex_trans = QTextEdit(trans)
        self.tex_trans.setFont(QFont("Timers",10,))
        
        self.img = QLabel('')
        self.pixmap = QPixmap(imname).scaled(200, 200)
        self.img.setPixmap(self.pixmap)

        self.palette1 = QPalette()
        self.padding = 0
        self.initGUI()
    def initGUI(self):

        v_box1 = QVBoxLayout()
        v_box1.addWidget(self.txt)
        v_box1.addWidget(self.tex_trans)##
        h_box1 =QHBoxLayout()
        h_box1.addWidget(self.img)
        h_box1.addLayout(v_box1)##
        v_box2 = QVBoxLayout()
        v_box2.addWidget(self.trans_button)
        v_box2.addLayout(h_box1)
        
        self.setLayout(v_box2)
        self.trans_button.clicked.connect(self.trans_again)# set geo
        self.setGeometry(750, 350, 460, 280)
        try:
            self.setWindowIcon(QIcon('/home/sun/Documents/APPs/screenshot_dict/icon.png'))#  set icon
        except Exception as e:
            print('setting icon failed')
        self.show()

    def trans_again(self):
        words = self.txt.toPlainText()
        # baidtrans API     
        # trans = baidutrans.trans(words)
        # if len(trans)>0 and 'trans_result' in trans: 
        #     trans = trans['trans_result'][0]['dst']
        #     self.tex_trans.setText(trans)
        trans = googletrans.trans_ch(words)
        self.tex_trans.setText(trans)


    def keyPressEvent(self, event):
        print('asdf')
        # if Qt.Key_D <= event.key() <= Qt.Key_D:
        #     # if event.modifiers() & Qt.ShiftModifier:
        #     #     self.key = "Shift+"
        if event.modifiers() & Qt.ControlModifier :
            print('dddddd')
            self.trans_again()

app = QApplication(sys.argv)
pad = TransApp()
sys.exit(app.exec_())