from PyQt5 import QtWidgets, uic
from time import sleep

janela = QtWidgets.QApplication([])
interface = uic.loadUi("telaLogin.ui")
tela2 = uic.loadUi("tela2.ui")

def segundaTela():
    tela2.show()
    interface.close()
    
def primeiraTela():
    interface.show()
    tela2.close()

interface.pushButtonLogin.clicked.connect(segundaTela)
tela2.pushButtonFechar.clicked.connect(primeiraTela)

interface.show()
janela.exec
