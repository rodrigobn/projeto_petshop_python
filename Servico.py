
class Servico:

    def __init__(self, id = 0, nome = '', valor = 0, descricao = ''):

        self.__id = id
        self.__nome = nome
        self.__valor = valor
        self.__descricao = descricao

    def getId(self):
        """
        Retorna o codigo do servico
        """
        return self.__id
    
    def setId(self, id):
        """
        Modifica o codigo do servico
        Parametro:
        - codigo novo do servico
        """
        self.__id = id
    
    def getNome(self):
        """
        Retorna o nome do servico
        """
        return self.__nome

    def setNome(self, nome):
        """
        Modifica o nome do servico
        Parametro:
        - nome corrigido do servico
        """
        self.__nome = nome
    
    def getDescricao(self):
        """
        Retorna a descricao do servico
        """
        return self.__descricao

    def setDescricao(self, descricao):
        """
        Modifica a descricao do servico
        Parametro:
        - descricao nova do servico
        """
        self.__descricao = descricao
    
    def getValor(self):
        """
        Retorna o valor do servico
        """
        return self.__valor

    def setValor(self, valor):
        """
        Modifica o valor do servico
        Parametro:
        - valor novo do servico
        """
        self.__valor = valor
    
    def valorTotalComDesconto(self, porcentagem = 0):
        return self.getValor() + (self.getValor() * porcentagem) / 100