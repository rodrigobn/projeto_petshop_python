
class Funcionario:

    def __init__(self, id = 0, nome = "", senha = 0000):
        """
        Cria um funcionario.
            Parametros :
            - id.
            - nome e opcional (padrao : "").
            - senha e opcional (padrao : 0000)
        """
        self.__id = id
        self.__nome = nome
        self.__senha = senha
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome
    
    def getsenha(self):
        return self.__senha
    
    def setSenha(self, senha):
        self.__senha = senha