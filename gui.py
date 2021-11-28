from PyQt5 import QtCore, QtGui, QtWidgets
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA1
import binascii
import os

def firmar(archivo, llave):

    filename = os.path.basename(archivo).split('.')
    output = f"{filename[0]}_Signed.{filename[1]}"
    
    with open(archivo) as f:
        mensaje = f.readlines()
        mensaje = ''.join(mensaje)
    mensaje = mensaje.encode()
    
    f = open(llave,'r')
    key = RSA.import_key(f.read())
    hash = SHA1.new(mensaje)
    signer = PKCS115_SigScheme(key)
    firma = signer.sign(hash)
    firma = binascii.hexlify(firma).decode('utf-8')
    texto = mensaje.decode('utf-8') + '\n' + firma

    archivo = open(output, 'w')
    archivo.write(texto)
    archivo.close()


def verificar(archivo, llave):

    file = open(archivo,'r')
    file = file.readlines()
    file = file[:-1]
    mensaje = ''
    for lines in file:
        mensaje += lines
    mensaje = mensaje[:-1]
    mensaje = mensaje.encode()

    with open(archivo, 'r') as f:
        for last_line  in f:
            pass

    firma = bytes.fromhex(last_line)

    key = RSA.import_key(open(llave).read())
    hash = SHA1.new(mensaje)
    verifier = PKCS115_SigScheme(key)
    try:
        verifier.verify(hash, firma)
        return True
    except:
        return False


class Ui_FirmaElectronica(object):

    fname = ''
    fkey = ''
    
    def setupUi(self, FirmaElectronica):
        FirmaElectronica.setObjectName("FirmaElectronica")
        FirmaElectronica.resize(700, 600)
        FirmaElectronica.setStyleSheet("background-color: rgb(202, 215, 227);")
        
        self.centralwidget = QtWidgets.QWidget(FirmaElectronica)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 0, 231, 231))
        self.label.setStyleSheet("image: url(:/imagenes/ipn.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 211, 151))
        self.label_2.setStyleSheet("image: url(:/imagenes/logoescom.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 40, 281, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(210, 250, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(410, 250, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 310, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.selArchivo)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 310, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 370, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.selLlave)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 370, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 520, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 430, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.continuar)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 480, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.generarKeys)

        FirmaElectronica.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FirmaElectronica)
        self.statusbar.setObjectName("statusbar")
        FirmaElectronica.setStatusBar(self.statusbar)

        self.retranslateUi(FirmaElectronica)
        QtCore.QMetaObject.connectSlotsByName(FirmaElectronica)

    def retranslateUi(self, FirmaElectronica):
        _translate = QtCore.QCoreApplication.translate
        FirmaElectronica.setWindowTitle(_translate("FirmaElectronica", "Firma Electronica"))
        self.label_3.setText(_translate("FirmaElectronica", "Pedroza García Rodolfo \n" "Pardo Alanis Arturo Isaac"))
        self.radioButton.setText(_translate("FirmaElectronica", "Firmar"))
        self.radioButton_2.setText(_translate("FirmaElectronica", "Verificar"))
        self.pushButton.setText(_translate("FirmaElectronica", "Seleccionar Archivo"))
        self.pushButton_2.setText(_translate("FirmaElectronica", "Seleccionar Llave"))
        self.pushButton_3.setText(_translate("FirmaElectronica", "Continuar"))
        self.pushButton_4.setText(_translate("FirmaElectronica", "Generar Firmas"))

    def selArchivo(self):
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(FirmaElectronica, 'Open a file', '', 'All files (*)')
        filename = os.path.basename(self.fname)
        self.fname = filename
        self.label_4.setText(filename)
    
    def selLlave(self):
        self.fkey, _ = QtWidgets.QFileDialog.getOpenFileName(FirmaElectronica, 'Open a file', '', 'All files (*)')
        filename = os.path.basename(self.fkey)
        self.fkey = filename
        self.label_5.setText(filename)

    def continuar(self):
        fname = self.fname
        fkey = self.fkey
        if self.radioButton.isChecked():
            firmar(fname, fkey)
        else:
            check = verificar(fname, fkey)
            if check:
                self.label_6.setText('Firma Valida')
            else:
                self.label_6.setText('Firma Invalida')

    
    def generarKeys(self):
        
        key_Alicia = RSA.generate(1024)
        private_key_Alicia= key_Alicia.export_key()
        file_out = open("LlavePrivadaAlicia.pem", "wb")
        file_out.write(private_key_Alicia)
        file_out.close()

        public_key_alice = key_Alicia.publickey().export_key()
        file_out = open("LlavePublicaAlicia.pem", "wb")
        file_out.write(public_key_alice)
        file_out.close()
        
        key_Betito = RSA.generate(1024)
        private_key_Betito = key_Betito.export_key()
        file_out = open("LlavePrivadaBetito.pem", "wb")
        file_out.write(private_key_Betito)
        file_out.close()

        public_key_Betito = key_Betito.publickey().export_key()
        file_out = open("LlavePublicaBetito.pem", "wb")
        file_out.write(public_key_Betito)
        file_out.close()
        
        key_Candy = RSA.generate(1024)
        private_key_Candy = key_Candy.export_key()
        file_out = open("LlavePrivadaCandy.pem", "wb")
        file_out.write(private_key_Candy)
        file_out.close()

        private_key_Candy = key_Candy.publickey().export_key()
        file_out = open("LlavePublicaCandy.pem", "wb")
        file_out.write(private_key_Candy)
        file_out.close()



import rs_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirmaElectronica = QtWidgets.QMainWindow()
    ui = Ui_FirmaElectronica()
    ui.setupUi(FirmaElectronica)
    FirmaElectronica.show()
    sys.exit(app.exec_())
