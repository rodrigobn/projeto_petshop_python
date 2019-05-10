
class Produto:

    def __init__(self, id = 0, nome = '', valor = 0, descricao = '', tipo = ''):

        self.__id = id
        self.__nome = nome
        self.__valor = valor
        self.__descricao = descricao
        self.__tipo = tipo

    def getId(self):
        """
        Retorna o codigo do produto
        """
        return self.__id
    
    def setId(self, id):
        """
        Modifica o codigo do produto
        Parametro:
        - codigo novo do produto
        """
        self.__id = id
    
    def getNome(self):
        """
        Retorna o nome do produto
        """
        return self.__nome

    def setNome(self, nome):
        """
        Modifica o nome do produto
        Parametro:
        - nome corrigido do produto
        """
        self.__nome = nome
    
    def getDescricao(self):
        """
        Retorna a descricao do produto
        """
        return self.__descricao

    def setDescricao(self, descricao):
        """
        Modifica a descricao do produto
        Parametro:
        - descricao nova do produto
        """
        self.__descricao = descricao
    
    def getValor(self):
        """
        Retorna o valor do produto
        """
        return self.__valor

    def setValor(self, valor):
        """
        Modifica o valor do produto
        Parametro:
        - valor novo do produto
        """
        self.__valor = valor

    def getTipo(self):
        """
        Retorna o tipo do produto
        """
        return self.__tipo
    
    def setTipo(self, tipo):
        """
        Modifica o tipo do produto
        Parametro:
        - tipo novo do produto
        """
        self.__tipo = tipo
    
    def valorTotalComDesconto(self, porcentagem = 0):
        return self.getValor() + (self.getValor() * porcentagem) / 100