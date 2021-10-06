from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto.Util.Padding import pad, unpad
import PIL.Image as Image
from Crypto.Cipher import DES
import os

def trans_format_RGB(data):
    #tuple: Immutable, ensure that data is not lost
    red, green, blue = tuple(map(lambda e: [data[i] for i in range(0, len(data)) if i % 3 == e], [0, 1, 2]))
    pixels = tuple(zip(red, green, blue))
    return pixels


def image_encrypt(fname, mode, iv, key):

    filename = os.path.basename(fname).split('.')
    img = Image.open(fname.encode())
    bImg = img.convert("RGB").tobytes()
    imgLen = len(bImg)
    
    if mode == "ECB":
        cipher = DES.new(key, DES.MODE_ECB)
        m = cipher.encrypt(pad(bImg, 8))
        enc_img = trans_format_RGB(m [:imgLen])
        im2 = Image.new(img.mode, img.size)
        im2.putdata(enc_img)
        im2.save(f"{filename[0]}_eECB.{filename[1]}")
        im2.show()
    elif mode == 'CBC':
        cipher = DES.new(key, DES.MODE_CBC, iv)
        m = cipher.encrypt(pad(bImg, 8))
        enc_img = trans_format_RGB(m [:imgLen])
        im2 = Image.new(img.mode, img.size)
        im2.putdata(enc_img)
        im2.save(f"{filename[0]}_eCBC.{filename[1]}")
        im2.show()
    elif mode == 'CFB':
        cipher = DES.new(key, DES.MODE_CFB, iv)
        m = cipher.encrypt(pad(bImg, 8))
        enc_img = trans_format_RGB(m [:imgLen])
        im2 = Image.new(img.mode, img.size)
        im2.putdata(enc_img)
        im2.save(f"{filename[0]}_eCFB.{filename[1]}")
        im2.show()
    else:
        cipher = DES.new(key, DES.MODE_OFB, iv)
        m = cipher.encrypt(pad(bImg, 8))
        enc_img = trans_format_RGB(m [:imgLen])
        im2 = Image.new(img.mode, img.size)
        im2.putdata(enc_img)
        im2.save(f"{filename[0]}_eOFB.{filename[1]}")
        im2.show()
    return 

def image_decrypt(fname, mode, iv, key):

    filename = os.path.basename(fname).split('.')

    img = Image.open(fname.encode())

    cImg = img.convert("RGB").tobytes()
    imgLen = len(cImg)

    if mode == "ECB":
        cipher = DES.new(key, DES.MODE_ECB)
        m = cipher.decrypt(pad(cImg, 8))
        decry_img = trans_format_RGB(m [:imgLen])
        im2 = Image.new(img.mode, img.size)
        im2.putdata(decry_img)
        im2.save(f"{filename[0]}_dECB.{filename[1]}")
        im2.show()
    elif mode == "CBC":
        cipher = DES.new(key, DES.MODE_CBC, iv)
        m = cipher.decrypt(pad(cImg, 8))
        decry_img = trans_format_RGB(m [:imgLen])
        im2 = Image.new(img.mode, img.size)
        im2.putdata(decry_img)
        im2.save(f"{filename[0]}_dCBC.{filename[1]}")
        im2.show()
    elif mode == "CFB":
        cipher = DES.new(key, DES.MODE_CFB, iv)
        m = cipher.decrypt(pad(cImg, 8))
        decry_img = trans_format_RGB(m [:imgLen])
        im2 = Image.new(img.mode, img.size)
        im2.putdata(decry_img)
        im2.save(f"{filename[0]}_dCFB.{filename[1]}")
        im2.show()
    else:
        cipher = DES.new(key, DES.MODE_OFB, iv)
        m = cipher.decrypt(pad(cImg, 8))
        decry_img = trans_format_RGB(m [:imgLen])
        im2 = Image.new(img.mode, img.size)
        im2.putdata(decry_img)
        im2.save(f"{filename[0]}_dOFB.{filename[1]}")
        im2.show()    
    return 



class Ui_Practica2(object):

    fname = ''

    def setupUi(self, Practica2):
        Practica2.setObjectName("Practica2")
        Practica2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Practica2)
        self.centralwidget.setObjectName("centralwidget")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(70, 320, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(270, 320, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 301, 151))
        self.label.setStyleSheet("image: url(:/logo1/logoescom.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 10, 281, 251))
        self.label_2.setStyleSheet("image: url(:/logo1/ipn.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 440, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.selArchivo)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 440, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 500, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 500, 113, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 500, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 500, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 100, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 380, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.modos("ECB"))

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 380, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.modos("CBC"))

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 380, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.modos("OFB"))

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 380, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda: self.modos("CFB"))

        Practica2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Practica2)
        self.statusbar.setObjectName("statusbar")
        Practica2.setStatusBar(self.statusbar)

        self.retranslateUi(Practica2)
        QtCore.QMetaObject.connectSlotsByName(Practica2)

    def retranslateUi(self, Practica2):
        _translate = QtCore.QCoreApplication.translate
        Practica2.setWindowTitle(_translate("Practica2", "Practica 2"))
        self.radioButton.setText(_translate("Practica2", "Cifrar"))
        self.radioButton_2.setText(_translate("Practica2", "Descifrar"))
        self.pushButton.setText(_translate("Practica2", "Archivo de entrada"))
        self.label_3.setText(_translate("Practica2", "Llave"))
        self.label_4.setText(_translate("Practica2", "VI"))
        self.label_5.setText(_translate("Practica2", "Pedroza García Rodolfo \n" "Pardo Alanis Arturo Isaac"))
        self.label_6.setText(_translate("Practica2", "Nombre del archivo"))
        self.pushButton_2.setText(_translate("Practica2", "ECB"))
        self.pushButton_3.setText(_translate("Practica2", "CBC"))
        self.pushButton_4.setText(_translate("Practica2", "OFB"))
        self.pushButton_6.setText(_translate("Practica2", "CFB"))

    def selArchivo(self):
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(Practica2, 'Open a file', '', 'Images (*.png *.jpg *.bmp)')
        filename = os.path.basename(self.fname)
        self.label_6.setText(filename)

    def modos(self, modo):
        llave = self.lineEdit.text()
        iv = self.lineEdit_2.text()
        # print("hola {m} {l}  {i} ".format(m=modo, l= llave, i = iv))

        if self.radioButton.isChecked():
            image_encrypt(self.fname , modo, iv.encode("utf8"), llave.encode())
        else:
            image_decrypt(self.fname , modo, iv.encode("utf8"), llave.encode())




import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Practica2 = QtWidgets.QMainWindow()
    ui = Ui_Practica2()
    ui.setupUi(Practica2)
    Practica2.show()
    sys.exit(app.exec_())
