#IMPORTANTO BIBLIOTECAS
#biblioteca grafica
from tkinter import *



class Application:
    def __init__(self, master=None):
        pass

def clique():
    janela2 = Tk()
    janela2.geometry("500x500+500+200")
    janela2.mainloop()
    janela.quit()    

#instancia uma frame(tela)
janela = Tk()

#Largura x Altura + ME(eixo x) + MT(eixo y)
janela.geometry("1350x750+0+0")

#Titulo da tela
janela.title("Tela Principal")

#background da tela(pode usar exadecimal ex: #707070)
janela.configure(background="#707070")

#CRINANDO PAINEIS(frame) INTERNOS nas posições topo, esquerda e direita
#frame(paineis, armações ou molduras) 
#parametros: tela, largura, altura, bd=intencidade do efeito, relief=efeito de relevo
top = Frame(janela, width=1350, height=60)
top.pack(side=TOP)

left = Frame(janela, width=900, height=640)
left.pack(side=LEFT)

right = Frame(janela, width=445, height=640)
right.pack(side=RIGHT)


#FRAMES SECUNDARIOS
#criando um painel que ira preencher a largura do painel right
#e depois um painel de mesma largura a baixo
rightPainel1 = Frame(right, width=445, height=600)
rightPainel1.pack(side=TOP) #Posição dentro do painel right
rightPainel1.configure(background='#92da1a')

rightPainel2 = Frame(right, width=445, height=40)
rightPainel2.pack(side=BOTTOM)
rightPainel2.configure(background='#7b3620')


leftPainel1 = Frame(left, width=900, height=400)
leftPainel1.pack(side=TOP) #Posição dentro do painel left
leftPainel1.configure(background='#92da1a')

leftPainel2 = Frame(left, width=900, height=240)
leftPainel2.pack(side=BOTTOM)
leftPainel2.configure(background='#7b3620')


#Label parametros: Local onde vai ficar, fonte,  texto, larg, altu)
lbLTitulo = Label(top, font=('arial', 40), text="PetShop", width=43, height=1)
lbLTitulo.grid(row=0, column=0)


#botão, parametros(tela que vai ser colocado, texto dp botão, altura, largura, comando do clique)
btnEmail = Button(janela, text="Email", width=10, height=2, command=clique)

#posição dos widgets
#lbLTitulo.grid(row=1, column=0)
#btnEmail.grid(row=1, column=1)




Application(janela)

janela.mainloop()

