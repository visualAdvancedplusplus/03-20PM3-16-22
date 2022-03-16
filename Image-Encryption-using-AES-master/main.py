from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QFileDialog,QLabel,QAction,QMainWindow,QApplication
from PyQt5.uic import loadUiType
from Encrypter import Encrypter
from Decrypter import Decrypter
from PIL import Image as Img
from PIL import ImageTk as ImgTk
import base64
from Crypto.Cipher import AES
import os
import sys






Qt = QtCore.Qt

ui, _ = loadUiType('ui.ui')
def start():
    global m
    m = Main_Window()
    m.show()
    
class encrypt_page():
    def __init__(self):
        self.file={}
        self.stri=""
        self.Handel_Buttons()
        self.pushButton_3.clicked.connect(self.chooseFile)
        self.pushButton_4.clicked.connect(self.onClickEncrypt)
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
    def chooseFile(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open File')
        pixmap = QtGui.QPixmap(self.file[0])
        self.lbl.setPixmap(pixmap.scaledToHeight(201))
        if self.file != None:
            ba = QtCore.QByteArray()
            buff = QtCore.QBuffer(ba)
            buff.open(QtCore.QIODevice.WriteOnly) 
            ok = pixmap.save(buff, "PNG")
            assert ok
            pixmap_bytes = ba.data()
            self.stri = base64.b64encode(pixmap_bytes)
        
    def onClickEncrypt(self):
        myKey=self.lineEdit.text()
        x = Encrypter(self.stri, myKey)
        cipher = x.encrypt_image()
        fh = open("cipher.txt", "wb")
        fh.write(cipher)
        fh.close()

class decrypt_page():
    def __init__(self):
        self.cipher={}
        self.Handel_Buttons()
        self.pushButton_5.clicked.connect(self.chooseFile1)
        self.pushButton_6.clicked.connect(self.onClickDecrypt)
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
    def chooseFile1(self):
        file = QFileDialog.getOpenFileName(self, 'Open File')
        text=open(file[0]).read()
        self.cipher= text.encode('utf-8')
    def onClickDecrypt(self):
        myKey=self.lineEdit_2.text()
        x = Decrypter(self.cipher)
        image=x.decrypt_image(myKey)
        ba = QtCore.QByteArray(image)
        pixmap = QtGui.QPixmap()
        ok = pixmap.loadFromData(ba, "PNG")
        assert ok        
        self.lbl_2.setPixmap(pixmap.scaledToHeight(201))
           
        
class Main_Window(QMainWindow, QWidget, ui,encrypt_page,decrypt_page):
    def __init__(self):
        QMainWindow.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)
        encrypt_page.__init__(self)
        decrypt_page.__init__(self)
        self.Handel_Buttons() 
        self.stackedWidget.setCurrentIndex(0)
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = start()
    app.exec_()
