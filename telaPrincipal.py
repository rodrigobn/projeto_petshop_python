from tkinter import *
from Sistema import *
import tkinter.messagebox as tkmsg

class TelaPrincipal():

    def __init__(self, master=None):
        self.largura = 800
        self.altura = 800
        #master.resizable(0, 0) # Tela de tamanho fixo
        self.fontePadrao = ('Arial', '12')
        self.sistema = Sistema()

        self.countainerLogo = Frame(master)
        self.countainerLogo['pady'] = 50 # distancia das bordas
        self.countainerLogo.grid_propagate(0) # (0)Desliga (1)Liga e não deixe que os widgets dentro do controle quadro do seu tamanho
        self.countainerLogo.grid() # plota no formado de grade

        self.titulo = Label(self.countainerLogo, text = 'LOGO', font=self.fontePadrao)
        self.titulo.pack()
'''
root = Tk()
TelaPrincipal(root)
root.mainloop()
'''