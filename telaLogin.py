from tkinter import *
from Sistema import *
from telaPrincipal import * 
import tkinter.messagebox as tkmsg

class TelaLogin():

    def __init__(self, master=None):
        
        self.janelaLogin = Tk()
        self.janelaLogin.title('Login')

        self.largura = 300
        self.altura =200
        #master.resizable(0, 0) # Tela de tamanho fixo
        self.fontePadrao = ('Arial', '12')
        self.sistema = Sistema()

        self.countainerLogo = Frame(master)
        self.countainerLogo['pady'] = 50 # distancia das bordas
        self.countainerLogo.grid_propagate(0) # (0)Desliga (1)Liga e não deixe que os widgets dentro do controle quadro do seu tamanho
        self.countainerLogo.grid() # plota no formado de grade

        self.titulo = Label(self.countainerLogo, text = 'LOGO', font=self.fontePadrao)
        self.titulo.pack()

        self.countainerFormulario = Frame(master)
        self.countainerFormulario['pady'] = 50
        self.countainerFormulario.grid()

        self.nomeLabel = Label(self.countainerFormulario, text = 'Nome:', font=self.fontePadrao)
        self.nomeLabel.grid(row=0,column=0, padx= 10, pady=0) # Seleciona a liha e a coluna na tela e as bordas de distancia

        self.nome = Entry(self.countainerFormulario)
        self.nome['width'] = 20
        self.nome['font'] = self.fontePadrao
        self.nome.grid(row=0,column=1, padx= 10, pady=10)
        
        self.campoSenhaLabel = Label(self.countainerFormulario, text = 'Senha:', font=self.fontePadrao)
        self.campoSenhaLabel.grid(row=1,column=0, padx= 10, pady=0)

        self.campoSenha = Entry(self.countainerFormulario)
        self.campoSenha['width'] = 20
        self.campoSenha['font'] = self.fontePadrao
        self.campoSenha.grid(row=1,column=1, padx= 10, pady=10)

        self.btnLogin = Button(self.countainerFormulario)
        self.btnLogin['text'] = 'Login'
        self.btnLogin['bg'] = 'green'
        self.btnLogin['fg'] = 'white'
        self.btnLogin['font'] = self.fontePadrao
        self.btnLogin['width'] = 20
        self.btnLogin['command'] = self.autenticacao
        self.btnLogin.grid(row=2,column=1, padx= 10, pady=10)

        self.countainerAddFuncionario = Frame(master)
        self.countainerAddFuncionario['pady'] = 10
        self.countainerAddFuncionario.grid()
        
        self.btnCadastraFuncionario = Button(self.countainerAddFuncionario)
        self.btnCadastraFuncionario['text'] = 'Cadastrar'
        self.btnCadastraFuncionario['bg'] = 'black'
        self.btnCadastraFuncionario['fg'] = 'white'
        self.btnCadastraFuncionario['font'] = self.fontePadrao
        self.btnCadastraFuncionario['width'] = 10
        self.btnCadastraFuncionario['command'] = self.cadastrarFuncionario
        self.btnCadastraFuncionario.grid(row=0,column=0, padx= 10, pady=10)

        self.btnRemoveFuncionario = Button(self.countainerAddFuncionario)
        self.btnRemoveFuncionario['text'] = 'Remover'
        self.btnRemoveFuncionario['bg'] = 'red'
        self.btnRemoveFuncionario['fg'] = 'white'
        self.btnRemoveFuncionario['font'] = self.fontePadrao
        self.btnRemoveFuncionario['width'] = 10
        self.btnRemoveFuncionario['command'] = self.removeFuncionario
        self.btnRemoveFuncionario.grid(row=0,column=1, padx= 10, pady=10)

        self.janelaLogin.mainloop() 

    
    def autenticacao(self):
        '''
        Verifica se contem o nome e a campoSenha na lista de funcionarios na classe Sistema
        '''
        if self.nome.get() != '' and self.campoSenha.get() != '':
            if self.sistema.login(self.nome.get(), self.campoSenha.get()):
                result = tkmsg.showinfo(title='Meu dialogo showinfo', message='Login realizado com sucesso')
                self.sair()
                janelaPrincipal = Tk()
                TelaPrincipal(janelaPrincipal)
                janelaPrincipal.mainloop()
                
            else:
                result = tkmsg.showinfo(title='Meu dialogo showinfo', message='Nome ou Senha invalidos')                

    def sair(self):
        '''
        Destroi a tela atual
        '''
        self.janelaLogin.destroy()

    def cadastrarFuncionario(self):
        self.janelaLogin.destroy()
        self.janelaCadastraFuncionario = Tk()
        self.janelaCadastraFuncionario.title('Cadastra Funcionario')
        
        self.countainerFormulario = Frame()
        self.countainerFormulario['pady'] = 50
        self.countainerFormulario.grid()

        self.nomeLabel = Label(self.countainerFormulario, text = 'Nome:', font=self.fontePadrao)
        self.nomeLabel.grid(row=0,column=0, padx= 10, pady=0) # Seleciona a liha e a coluna na tela e as bordas de distancia

        self.campoNome = Entry(self.countainerFormulario)
        self.campoNome['width'] = 20
        self.campoNome['font'] = self.fontePadrao
        self.campoNome.grid(row=0,column=1, padx= 10, pady=10)
        
        self.campoSenhaLabel = Label(self.countainerFormulario, text = 'Senha:', font=self.fontePadrao)
        self.campoSenhaLabel.grid(row=1,column=0, padx= 10, pady=0)

        self.campoSenha = Entry(self.countainerFormulario)
        self.campoSenha['width'] = 20
        self.campoSenha['font'] = self.fontePadrao
        self.campoSenha.grid(row=1,column=1, padx= 10, pady=10)

        self.btnCadastraFuncionario = Button(self.countainerFormulario)
        self.btnCadastraFuncionario['text'] = 'Cadastrar'
        self.btnCadastraFuncionario['bg'] = 'green'
        self.btnCadastraFuncionario['fg'] = 'white'
        self.btnCadastraFuncionario['font'] = self.fontePadrao
        self.btnCadastraFuncionario['width'] = 20
        self.btnCadastraFuncionario['command'] = self.confirmaCadastro
        self.btnCadastraFuncionario.grid(row=2,column=1, padx= 10, pady=10)


        self.janelaCadastraFuncionario.mainloop()

    def confirmaCadastro(self):
        '''
        Faz o cadastro do Funcionario e fecha a janela de cadastro.
        '''
        if self.campoNome.get() != '' and self.campoSenha.get() != '':
            self.sistema.cadastraFuncionario(self.campoNome.get(), self.campoSenha.get())
            self.sistema.salvaArquivo()
            resultado = tkmsg.showinfo(title='Confirmação', message='Cadastrado com sucesso!')

            #self.sistema.abreArquivoFuncionarios()
            
            self.janelaCadastraFuncionario.destroy()
            TelaLogin() 
        else:
            resultado = tkmsg.showinfo(title='Meu dialogo showinfo', message='Nome ou Senha invalidos')
        
    
    def removeFuncionario(self):
        self.janelaLogin.destroy()
        self.janelaRemoveFuncionario = Tk()
        self.janelaRemoveFuncionario.title('Remove Funcionario')
        
        self.countainerFormulario = Frame()
        self.countainerFormulario['pady'] = 50
        self.countainerFormulario.grid()

        self.nomeLabel = Label(self.countainerFormulario, text = 'Nome:', font=self.fontePadrao)
        self.nomeLabel.grid(row=0,column=0, padx= 10, pady=0) # Seleciona a liha e a coluna na tela e as bordas de distancia

        self.campoNome = Entry(self.countainerFormulario)
        self.campoNome['width'] = 20
        self.campoNome['font'] = self.fontePadrao
        self.campoNome.grid(row=0,column=1, padx= 10, pady=10)

        self.btnRemoveFuncionario = Button(self.countainerFormulario)
        self.btnRemoveFuncionario['text'] = 'Remover'
        self.btnRemoveFuncionario['bg'] = 'red'
        self.btnRemoveFuncionario['fg'] = 'white'
        self.btnRemoveFuncionario['font'] = self.fontePadrao
        self.btnRemoveFuncionario['width'] = 20
        self.btnRemoveFuncionario['command'] = self.confirmaRemocao
        self.btnRemoveFuncionario.grid(row=2,column=1, padx= 10, pady=10)


        self.janelaRemoveFuncionario.mainloop()

    def confirmaRemocao(self):
        '''
        Faz a remoção de um Funcionario e fecha a janela de remoção.
        '''
        if self.campoNome.get() != '':
            if self.sistema.removeFuncionario(self.campoNome.get()):
                self.sistema.salvaArquivo()
                tkmsg.showinfo(title='Confirmação', message='Removido com sucesso!')
            
                self.janelaRemoveFuncionario.destroy()
                TelaLogin()
            else:
                tkmsg.showinfo(title='Confirmação', message='Funcionario não existe')
                self.janelaRemoveFuncionario.destroy()
                TelaLogin()
        else:
            tkmsg.showinfo(title='Confirmação', message='Nome invalido')



TelaLogin()