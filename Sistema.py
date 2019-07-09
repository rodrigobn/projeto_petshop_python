from Cliente import *
from Pet import *
from Funcionario import *
from Produto import *
from Servico import *
import pickle
import shelve

class Sistema():
    def __init__(self):
        self.clientes = [] #shelve.open('arquivos/clientes.txt')['listas']
        self.produtos = [] #shelve.open('arquivos/produtos.txt')['listas']
        self.servicos = [] #shelve.open('arquivos/servicos.txt')['listas']
        self.funcionarios = self.abreArquivoFuncionarios() #shelve.open('arquivos/funcionarios.txt')['listas']

    def login(self, nome, senha):
        '''
        Verifica se existe um Funcionario na lista do sistema com o mesmo nome e senha. \n
        
        Parametros: \n
        Nome do funcionario\n
        Senha do funcionario\n
        
        return: boolean
        '''
        for i in self.funcionarios:
            if i.getNome() == nome and i.getSenha() == senha:
                return True
        return False

    def cadastraFuncionario(self, nome, senha):
        '''
        Adiciona um funcionario na lista do sistema, se não ouver funcionario o id = 1, caso haja o id é atualizado.\n
        Parametros: \n
        Nome do funcionario\n
        Senha do funcionario\n
        '''
        if len(self.funcionarios) > 0:
            funcionario = Funcionario(self.funcionarios[-1].getId()+1, nome, senha)
            self.funcionarios.append(funcionario)
        else:
            funcionario = Funcionario(1, nome, senha)
            self.funcionarios.append(funcionario)
    
    def removeFuncionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.getNome() == nome:
                self.funcionarios.remove(funcionario)
                return True
        
        return False
    
    def menuPrincipal(self):
        pass

    def aberturaCaixa(self):
        pass

    def salvaArquivo(self):
        funcionarios = shelve.open('arquivos/funcionarios.txt')
        funcionarios['lista'] = self.funcionarios
        
    
    def abreArquivoFuncionarios(self):
        funcionarios = shelve.open('arquivos/funcionarios.txt')
        return funcionarios['lista']
      

'''
sistema = Sistema()
sistema.salvaArquivo()
sistema.abreArquivo()
'''