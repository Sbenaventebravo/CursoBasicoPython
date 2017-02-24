# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '3enraya.ui'
#
# Created: Fri Feb 24 10:31:52 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Ventana(object):

    def setupUi(self, Ventana):
        Ventana.setObjectName(_fromUtf8("Ventana"))
        Ventana.resize(500, 320)
        Ventana.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Ventana.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.b0 = QtGui.QPushButton(Ventana)
        self.b0.setGeometry(QtCore.QRect(10, 10, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.b0.setFont(font)
        self.b0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b0.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);"))
        self.b0.setText(_fromUtf8(""))
        self.b0.setObjectName(_fromUtf8("b0"))
        self.b3 = QtGui.QPushButton(Ventana)
        self.b3.setGeometry(QtCore.QRect(10, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.b3.setFont(font)
        self.b3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b3.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);"))
        self.b3.setText(_fromUtf8(""))
        self.b3.setObjectName(_fromUtf8("b3"))
        self.b6 = QtGui.QPushButton(Ventana)
        self.b6.setGeometry(QtCore.QRect(10, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.b6.setFont(font)
        self.b6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b6.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);"))
        self.b6.setText(_fromUtf8(""))
        self.b6.setObjectName(_fromUtf8("b6"))
        self.b7 = QtGui.QPushButton(Ventana)
        self.b7.setGeometry(QtCore.QRect(110, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.b7.setFont(font)
        self.b7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b7.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);"))
        self.b7.setText(_fromUtf8(""))
        self.b7.setObjectName(_fromUtf8("b7"))
        self.b4 = QtGui.QPushButton(Ventana)
        self.b4.setGeometry(QtCore.QRect(110, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.b4.setFont(font)
        self.b4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b4.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);"))
        self.b4.setText(_fromUtf8(""))
        self.b4.setObjectName(_fromUtf8("b4"))
        self.b1 = QtGui.QPushButton(Ventana)
        self.b1.setGeometry(QtCore.QRect(110, 10, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.b1.setFont(font)
        self.b1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b1.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);"))
        self.b1.setText(_fromUtf8(""))
        self.b1.setObjectName(_fromUtf8("b1"))
        self.b8 = QtGui.QPushButton(Ventana)
        self.b8.setGeometry(QtCore.QRect(210, 210, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.b8.setFont(font)
        self.b8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b8.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);"))
        self.b8.setText(_fromUtf8(""))
        self.b8.setObjectName(_fromUtf8("b8"))
        self.b2 = QtGui.QPushButton(Ventana)
        self.b2.setGeometry(QtCore.QRect(210, 10, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.b2.setFont(font)
        self.b2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b2.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);"))
        self.b2.setText(_fromUtf8(""))
        self.b2.setObjectName(_fromUtf8("b2"))
        self.b5 = QtGui.QPushButton(Ventana)
        self.b5.setGeometry(QtCore.QRect(210, 110, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.b5.setFont(font)
        self.b5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b5.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);"))
        self.b5.setText(_fromUtf8(""))
        self.b5.setObjectName(_fromUtf8("b5"))
        self.ePuntaje = QtGui.QLabel(Ventana)
        self.ePuntaje.setGeometry(QtCore.QRect(340, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ePuntaje.setFont(font)
        self.ePuntaje.setObjectName(_fromUtf8("ePuntaje"))
        self.eMaquina = QtGui.QLabel(Ventana)
        self.eMaquina.setGeometry(QtCore.QRect(330, 80, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.eMaquina.setFont(font)
        self.eMaquina.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.eMaquina.setObjectName(_fromUtf8("eMaquina"))
        self.eEmpates = QtGui.QLabel(Ventana)
        self.eEmpates.setGeometry(QtCore.QRect(330, 130, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.eEmpates.setFont(font)
        self.eEmpates.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.eEmpates.setObjectName(_fromUtf8("eEmpates"))
        self.eYo = QtGui.QLabel(Ventana)
        self.eYo.setGeometry(QtCore.QRect(330, 170, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.eYo.setFont(font)
        self.eYo.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.eYo.setObjectName(_fromUtf8("eYo"))
        self.leMaquina = QtGui.QLineEdit(Ventana)
        self.leMaquina.setEnabled(False)
        self.leMaquina.setGeometry(QtCore.QRect(400, 70, 51, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.leMaquina.setFont(font)
        self.leMaquina.setObjectName(_fromUtf8("leMaquina"))
        self.leEmpates = QtGui.QLineEdit(Ventana)
        self.leEmpates.setEnabled(False)
        self.leEmpates.setGeometry(QtCore.QRect(400, 120, 51, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.leEmpates.setFont(font)
        self.leEmpates.setObjectName(_fromUtf8("leEmpates"))
        self.leYo = QtGui.QLineEdit(Ventana)
        self.leYo.setEnabled(False)
        self.leYo.setGeometry(QtCore.QRect(400, 160, 51, 25))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.leYo.setFont(font)
        self.leYo.setObjectName(_fromUtf8("leYo"))
        self.btnReiniciar = QtGui.QPushButton(Ventana)
        self.btnReiniciar.setGeometry(QtCore.QRect(360, 250, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnReiniciar.setFont(font)
        self.btnReiniciar.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 0);"))
        self.btnReiniciar.setObjectName(_fromUtf8("btnReiniciar"))

        self.retranslateUi(Ventana)
        QtCore.QMetaObject.connectSlotsByName(Ventana)

    def retranslateUi(self, Ventana):
        Ventana.setWindowTitle(_translate("Ventana", "3 En Raya", None))
        self.ePuntaje.setText(_translate("Ventana", "Puntaje", None))
        self.eMaquina.setText(_translate("Ventana", "Maquina", None))
        self.eEmpates.setText(_translate("Ventana", "Empates", None))
        self.eYo.setText(_translate("Ventana", "Yo", None))
        self.leMaquina.setText(_translate("Ventana", "0", None))
        self.leEmpates.setText(_translate("Ventana", "0", None))
        self.leYo.setText(_translate("Ventana", "0", None))
        self.btnReiniciar.setText(_translate("Ventana", "Reiniciar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Ventana = QtGui.QWidget()
    ui = Ui_Ventana()
    ui.setupUi(Ventana)
    Ventana.show()
    sys.exit(app.exec_())

