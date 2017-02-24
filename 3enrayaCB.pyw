from PyQt4 import QtCore, QtGui
import tresenraya
import sys
import random


class Ventana3EnRaya(QtGui.QMainWindow):
    def __init__(self, parent=None):
        self.tablero = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.movimientos = 0

        QtGui.QWidget.__init__(self, parent)
        self.ui = tresenraya.Ui_Ventana()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.b0, QtCore.SIGNAL("clicked()"), self.jugarenb0_click)
        QtCore.QObject.connect(self.ui.b1, QtCore.SIGNAL("clicked()"), self.jugarenb1_click)
        QtCore.QObject.connect(self.ui.b2, QtCore.SIGNAL("clicked()"), self.jugarenb2_click)
        QtCore.QObject.connect(self.ui.b3, QtCore.SIGNAL("clicked()"), self.jugarenb3_click)
        QtCore.QObject.connect(self.ui.b4, QtCore.SIGNAL("clicked()"), self.jugarenb4_click)
        QtCore.QObject.connect(self.ui.b5, QtCore.SIGNAL("clicked()"), self.jugarenb5_click)
        QtCore.QObject.connect(self.ui.b6, QtCore.SIGNAL("clicked()"), self.jugarenb6_click)
        QtCore.QObject.connect(self.ui.b7, QtCore.SIGNAL("clicked()"), self.jugarenb7_click)
        QtCore.QObject.connect(self.ui.b8, QtCore.SIGNAL("clicked()"), self.jugarenb8_click)
        QtCore.QObject.connect(self.ui.btnReiniciar, QtCore.SIGNAL("clicked()"), self.reiniciar)

    def jugarenb0_click(self):
        self.jugada(self.ui.b0)
        pass

    def jugarenb1_click(self):
        self.jugada(self.ui.b1)
        pass

    def jugarenb2_click(self):
        self.jugada(self.ui.b2)
        pass

    def jugarenb3_click(self):
        self.jugada(self.ui.b3)
        pass

    def jugarenb4_click(self):
        self.jugada(self.ui.b4)
        pass

    def jugarenb5_click(self):
        self.jugada(self.ui.b5)
        pass

    def jugarenb6_click(self):
        self.jugada(self.ui.b6)
        pass

    def jugarenb7_click(self):
        self.jugada(self.ui.b7)
        pass

    def jugarenb8_click(self):
        self.jugada(self.ui.b8)
        pass

    def colocar_ficha(self):
        while self.tablero.count(0):
            i = random.randrange(9)
            boton_maquina = self.ui.__dict__['b'+str(i)]
            if not self.tablero[i]:
                self.tablero[i] = 2
                boton_maquina.setText('0')
                boton_maquina.setEnabled(False)
                return True

    def jugada(self, boton):
        boton.setEnabled(False)
        boton.setText('X')
        self.tablero[int(list(boton.objectName())[1])] = 1
        self.movimientos += 1

        if self.verificar_jugada(1):
            yo = str(int(self.ui.leYo.displayText()) + 1)
            self.ui.leYo.setText(yo)
            self.congelar()
            return
        elif self.colocar_ficha():
            self.movimientos += 1
            if self.verificar_jugada(2):
                maquina = str(int(self.ui.leMaquina.displayText()) + 1)
                self.ui.leMaquina.setText(maquina)
                self.congelar()
                return
        if self.movimientos == 9:
            empate = str(int(self.ui.leEmpates.displayText()) + 1)
            self.ui.leEmpates.setText(empate)
        pass

    def congelar(self):
        i = 0
        while i < 9:
            self.ui.__dict__['b'+str(i)].setEnabled(False)
            i += 1

    def verificar_jugada(self, valor):
        if self.tablero[0] == self.tablero[1] == self.tablero[2] == valor:
            self.pintar(0, 1, 2)
            return 1
        if self.tablero[3] == self.tablero[4] == self.tablero[5] == valor:
            self.pintar(3, 4, 5)
            return 1
        if self.tablero[6] == self.tablero[7] == self.tablero[8] == valor:
            self.pintar(6, 7, 8)
            return 1
        if self.tablero[0] == self.tablero[3] == self.tablero[6] == valor:
            self.pintar(0, 3, 6)
            return 1
        if self.tablero[1] == self.tablero[4] == self.tablero[7] == valor:
            self.pintar(1, 4, 7)
            return 1
        if self.tablero[2] == self.tablero[5] == self.tablero[8] == valor:
            self.pintar(2, 5, 8)
            return 1
        if self.tablero[0] == self.tablero[4] == self.tablero[8] == valor:
            self.pintar(0, 4, 8)
            return 1
        if self.tablero[2] == self.tablero[4] == self.tablero[6] == valor:
            self.pintar(2, 4, 6)
            return 1
        pass

    def pintar(self, a, b, c):
        self.ui.__dict__['b'+str(a)].setStyleSheet(QtCore.QString.fromUtf8("color: rgb(100, 0, 100)"))
        self.ui.__dict__['b' + str(b)].setStyleSheet(QtCore.QString.fromUtf8("color: rgb(100, 0, 100)"))
        self.ui.__dict__['b' + str(c)].setStyleSheet(QtCore.QString.fromUtf8("color: rgb(100, 0, 100)"))
        pass

    def reiniciar(self):
        self.tablero= [0 for i in xrange(9)]
        self.movimientos = 0
        i = 0
        while i < 9:
            self.ui.__dict__['b'+str(i)].setEnabled(True)
            self.ui.__dict__['b' + str(i)].setText('')
            self.ui.__dict__['b' + str(i)].setStyleSheet(QtCore.QString.fromUtf8("background-color: #0E7AC4; color: rgb(255,255,255);"))
            i += 1

        pass
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Ventana = Ventana3EnRaya()
    Ventana.show()
    sys.exit(app.exec_())
