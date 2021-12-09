from PyQt5 import QtCore, QtGui, QtWidgets
import os
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA1
from Crypto.PublicKey import RSA
import binascii
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64encode
from base64 import b64decode


class Ui_CritpgrafiaHibrida(object):
    def setupUi(self, CritpgrafiaHibrida):

        fname= ''
        llavePublica= ''
        llavePrivada= ''
        iv= ''

        CritpgrafiaHibrida.setObjectName("CritpgrafiaHibrida")
        CritpgrafiaHibrida.resize(800, 600)
        CritpgrafiaHibrida.setStyleSheet("background-color: rgb(234, 215, 225);")
        self.centralwidget = QtWidgets.QWidget(CritpgrafiaHibrida)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 220, 611, 341))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_2 = QtWidgets.QPushButton(self.widget)        
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(189, 151, 196);\n" "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.firmar)
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        

        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(189, 151, 196);\n" "color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.verificar)
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.clicked.connect(self.cifrar)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(189, 151, 196);\n" "color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.clicked.connect(self.descifrar)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(189, 151, 196);\n" "color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(189, 151, 196);\n" "color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.descifrarVerificar)
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)

        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(189, 151, 196);\n" "color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.cifrarFirmar)
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)

        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 0, 721, 211))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setStyleSheet("image: url(:/img/logoescom.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.label_3 = QtWidgets.QLabel(self.widget1)        
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)

        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setStyleSheet("image: url(:/img/ipn.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        CritpgrafiaHibrida.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CritpgrafiaHibrida)
        self.statusbar.setObjectName("statusbar")
        CritpgrafiaHibrida.setStatusBar(self.statusbar)

        self.retranslateUi(CritpgrafiaHibrida)
        QtCore.QMetaObject.connectSlotsByName(CritpgrafiaHibrida)


    def retranslateUi(self, CritpgrafiaHibrida):
        _translate = QtCore.QCoreApplication.translate
        CritpgrafiaHibrida.setWindowTitle(_translate("CritpgrafiaHibrida", "Criptografía Híbrida "))
        self.pushButton_2.setText(_translate("CritpgrafiaHibrida", "Firmar"))
        self.pushButton_4.setText(_translate("CritpgrafiaHibrida", "Verificar"))
        self.pushButton.setText(_translate("CritpgrafiaHibrida", "Cifrar"))
        self.pushButton_3.setText(_translate("CritpgrafiaHibrida", "Descifrar"))
        self.pushButton_6.setText(_translate("CritpgrafiaHibrida", "Descifrar Y Verificar"))
        self.pushButton_5.setText(_translate("CritpgrafiaHibrida", "Cifrar Y Firmar"))
        self.label_3.setText(_translate("CritpgrafiaHibrida", "Criptografía Híbrida \n" "Pedroza García Rodolfo \n" "Pardo Alanis Arturo Isaac"))

    def cifrar(self):
        # Abrir Archivo
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar el archivo para Cifrar")
        dialog.exec_()
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'All files (*)')

        # abrir llave publica
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar la llave publica del receptor")
        dialog.exec_()
        self.llavePublica, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'pem files (*.pem)')

        filename = os.path.basename(self.fname)
        llavePublica = os.path.basename(self.llavePublica)

        archivo = os.path.basename(filename).split('.')
        output = f"{archivo[0]}Cifrado.{archivo[1]}"

        with open(filename) as f:
            mensaje = f.readlines()
            mensaje = ''.join(mensaje)
        mensaje = mensaje.encode()
        # print(mensaje)

        keyAES = get_random_bytes(16)
        cipher = AES.new(keyAES, AES.MODE_CBC)

        textoCifrado = cipher.encrypt(pad(mensaje, AES.block_size))
        textoCifrado = b64encode(textoCifrado).decode()
        vector = b64encode(cipher.iv).decode()

        print("texto:",textoCifrado)
        print("vector:",vector)
        
        #cifrar llave AES con RSA
        keyRSA = RSA.import_key(open(llavePublica).read())
        cipher = PKCS1_OAEP.new(keyRSA)
        llaveCifrada = cipher.encrypt(keyAES)
        llaveCifrada = b64encode(llaveCifrada).decode()

        print("keyAESCifrada:",llaveCifrada)

        texto = textoCifrado + '\n-------------------------\n' + vector + '\n-------------------------\n' + llaveCifrada
        archivo = open(output, 'w')
        archivo.write(texto)
        archivo.close()

    def descifrar(self):
        # Abrir Archivo
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar el archivo para decifrar")
        dialog.exec_()
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'All files (*)')

        # abrir llave privada
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar la llave Privada del receptor")
        dialog.exec_()
        self.llavePrivada, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'pem files (*.pem)')

        filename = os.path.basename(self.fname)
        llavePrivada = os.path.basename(self.llavePrivada)

        archivo = os.path.basename(filename).split('.')
        output = f"{archivo[0]}Decifrado.{archivo[1]}"

        with open(filename) as f:
            fileContent = f.readlines()
            fileContent = ''.join(fileContent)
        fileContent = fileContent.encode()
        contenido = fileContent.split(b"\n-------------------------\n")

        textoCifrado = contenido[0]
        iv = contenido[1]
        iv = b64decode(iv)
        keyAESCifrada = (contenido[2])
        keyAESCifrada = b64decode(keyAESCifrada)

        # decifrar llave aes
        keyRSA = RSA.import_key(open(llavePrivada).read())
        cipher = PKCS1_OAEP.new(keyRSA)
        keyAESDescifrada = cipher.decrypt(keyAESCifrada)


        #decifrar mensaje
        textoCifrado = b64decode(textoCifrado)
        cipher = AES.new(keyAESDescifrada, AES.MODE_CBC, iv)
        textoDecifrado = unpad(cipher.decrypt(textoCifrado), AES.block_size)
        textoDecifrado = textoDecifrado.decode()
        
        archivo = open(output, 'w')
        archivo.write(textoDecifrado)
        archivo.close()

    def firmar(self):
        # Abrir Archivo
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar el archivo para Firmar")
        dialog.exec_()
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'All files (*)')

        # abrir llave Privada
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar la llave Privada de quien va a firmar")
        dialog.exec_()
        self.llavePrivada, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'pem files (*.pem)')

        archivo = os.path.basename(self.fname)
        llavePrivada = os.path.basename(self.llavePrivada)

        filename = os.path.basename(archivo).split('.')
        output = f"{filename[0]}Firmado.{filename[1]}"
        
        with open(archivo) as f:
            fileContent = f.readlines()
            fileContent = ''.join(fileContent)
        fileContent = fileContent.encode()
        contenido = fileContent.split(b"\n-------------------------\n")

        mensaje = contenido[0]
        print("mensaje",mensaje)
        salida = contenido
        print(salida)

        f = open(llavePrivada,'r')
        key = RSA.import_key(f.read())
        digest = SHA1.new(mensaje)
        signer = PKCS115_SigScheme(key)
        firma = signer.sign(digest)
        firma = binascii.hexlify(firma).decode('utf-8')

        archivo = open(output, 'w')
        for element in contenido:
            archivo.write(element.decode() +'\n-------------------------\n')
        archivo.write(firma)
        archivo.close()

    def verificar(self):
        # Abrir Archivo
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar el archivo para Verificar")
        dialog.exec_()
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'All files (*)')

        # abrir llave Publica
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar la llave Publica de quien firmo")
        dialog.exec_()
        self.llavePublica, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'pem files (*.pem)')

        archivo = os.path.basename(self.fname)
        llavePublica = os.path.basename(self.llavePublica)

        with open(archivo) as f:
            fileContent = f.readlines()
            fileContent = ''.join(fileContent)
        fileContent = fileContent.encode()
        contenido = fileContent.split(b"\n-------------------------\n")

        mensaje = contenido[0]
        print(mensaje)
        firma = contenido[-1].decode()
        firma = bytes.fromhex(firma)

        key = RSA.import_key(open(llavePublica).read())
        digest = SHA1.new(mensaje)
        verifier = PKCS115_SigScheme(key)

        try:
            # Verificamos la firma
            verifier.verify(digest, firma)

            dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
            dialog.setWindowTitle("Alerta")
            dialog.setText("La llave es valida")
            dialog.exec_()
        except:
            dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
            dialog.setWindowTitle("Alerta")
            dialog.setText("La llave no es valida")
            dialog.exec_()
    
    def cifrarFirmar(self):
        #se necesita llave publica de quien recibe, para decifrarlo y la llave privada de quien firma
        # abrir archivo
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar el archivo para Cifrar")
        dialog.exec_()
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'All files (*)')

        # abrir llave publica
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar la llave publica del receptor")
        dialog.exec_()
        self.llavePublica, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'pem files (*.pem)')

        # abrir llave Privada
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar la llave Privada de quien va a firmar")
        dialog.exec_()
        self.llavePrivada, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'pem files (*.pem)')

        archivo = os.path.basename(self.fname)
        llavePublica = os.path.basename(self.llavePublica)
        llavePrivada = os.path.basename(self.llavePrivada)

        filename = os.path.basename(archivo).split('.')
        output = f"{filename[0]}CifradoFirmado.{filename[1]}"

        #leer mensaje
        with open(archivo) as f:
            mensaje = f.readlines()
            mensaje = ''.join(mensaje)
        mensaje = mensaje.encode()
        # print(mensaje)

        keyAES = get_random_bytes(16)
        cipher = AES.new(keyAES, AES.MODE_CBC)

        textoCifrado = cipher.encrypt(pad(mensaje, AES.block_size))
        textoCifrado = b64encode(textoCifrado)
        vector = b64encode(cipher.iv).decode()

        print("texto:",textoCifrado)
        # print("vector:",vector)
        
        #cifrar llave AES con RSA
        keyRSA = RSA.import_key(open(llavePublica).read())
        cipher = PKCS1_OAEP.new(keyRSA)
        llaveCifrada = cipher.encrypt(keyAES)
        llaveCifrada = b64encode(llaveCifrada).decode()

        # print("keyAESCifrada:",llaveCifrada)

        #firmar el mensaje
        f = open(llavePrivada,'r')
        key = RSA.import_key(f.read())
        digest = SHA1.new(textoCifrado)
        signer = PKCS115_SigScheme(key)
        firma = signer.sign(digest)
        firma = binascii.hexlify(firma).decode('utf-8')

        # print("firma", firma)
        textoCifrado = textoCifrado.decode()
        print(textoCifrado)
        archivo = open(output, 'w')
        archivo.write(textoCifrado + '\n-------------------------\n')
        archivo.write(vector + '\n-------------------------\n')
        archivo.write(llaveCifrada + '\n-------------------------\n')
        archivo.write(firma)
        archivo.close()

    def descifrarVerificar(self):
        #archivo cifrado, llave privada de quien descifra, y llave publica de quien firmo
        # abrir archivo
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar el archivo para Descifrar")
        dialog.exec_()
        self.fname, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'All files (*)')

        # abrir llave publica
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar la llave publica de quien firmo")
        dialog.exec_()
        self.llavePublica, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'pem files (*.pem)')

        # abrir llave Privada
        dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
        dialog.setWindowTitle("Abrir Archivo")
        dialog.setText("Seleccionar la llave Privada de quien va a descifrar")
        dialog.exec_()
        self.llavePrivada, _ = QtWidgets.QFileDialog.getOpenFileName(CritpgrafiaHibrida, 'Open a file', '', 'pem files (*.pem)')

        archivo = os.path.basename(self.fname)
        llavePublica = os.path.basename(self.llavePublica)
        llavePrivada = os.path.basename(self.llavePrivada)

        filename = os.path.basename(archivo).split('.')
        output = f"{filename[0]}VerificadoDescifrado.{filename[1]}"

        #leer archivo
        with open(archivo) as f:
            fileContent = f.readlines()
            fileContent = ''.join(fileContent)
        fileContent = fileContent.encode()
        contenido = fileContent.split(b"\n-------------------------\n")

        textoCifrado = contenido[0]
        iv = contenido[1]
        iv = b64decode(iv)
        keyAESCifrada = (contenido[2])
        keyAESCifrada = b64decode(keyAESCifrada)
        firma = contenido[-1].decode()
        firma = bytes.fromhex(firma)

        print(textoCifrado)
        print(iv)
        print(firma)

        key = RSA.import_key(open(llavePublica).read())
        digest = SHA1.new(textoCifrado)
        verifier = PKCS115_SigScheme(key)

        try:
            # Verificamos la firma
            verifier.verify(digest, firma)

            dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
            dialog.setWindowTitle("Alerta")
            dialog.setText("La llave es valida. Archivo descifrado")
            dialog.exec_()

            # decifrar llave aes
            keyRSA = RSA.import_key(open(llavePrivada).read())
            cipher = PKCS1_OAEP.new(keyRSA)
            keyAESDescifrada = cipher.decrypt(keyAESCifrada)


            #decifrar mensaje
            textoCifrado = b64decode(textoCifrado)
            cipher = AES.new(keyAESDescifrada, AES.MODE_CBC, iv)
            textoDecifrado = unpad(cipher.decrypt(textoCifrado), AES.block_size)
            textoDecifrado = textoDecifrado.decode()
            
            archivo = open(output, 'w')
            archivo.write(textoDecifrado)
            archivo.close()


        except:
            dialog = QtWidgets.QMessageBox(CritpgrafiaHibrida)
            dialog.setWindowTitle("Alerta")
            dialog.setText("La llave no es valida")
            dialog.exec_()


import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CritpgrafiaHibrida = QtWidgets.QMainWindow()
    ui = Ui_CritpgrafiaHibrida()
    ui.setupUi(CritpgrafiaHibrida)
    CritpgrafiaHibrida.show()
    sys.exit(app.exec_())
