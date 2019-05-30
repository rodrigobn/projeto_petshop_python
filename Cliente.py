from Pet import Pet

class Cliente:
    """
        Cria um cliente.
        Parametros :
        - id.
        - nome e opcional (padrao : "").
        - idade e opcional (padrao : 0)
        - telefone e opcional (padrao : "").
        - endereco e opcional (padrao : "")..
        - CPF e opcional (padrao : "").
        """
    def __init__(self, id = 0, nome = "", idade = 0, telefone = "", endereco = "", cpf = ""):
        
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf
        self.__pets = []
        self.__produtos = []
        self.__servicos = []
    
    def getid(self):
        """
        Retorna o codigo do cliente
        """
        return self.__id
    
    def setid(self, id):
        """
        Modifica o codigo do cliente
        Parametro:
        - codigo novo do cliente
        """
        self.__id = id
    
    def getNome(self):
        """
        Retorna o nome do cliente
        """
        return self.__nome

    def setNome(self, nome):
        """
        Modifica o nome do cliente
        Parametro:
        - nome corrigido do cliente
        """
        self.__nome = nome
    
    def getIdade(self):
        """
        Retorna a idade do cliente
        """
        return self.__idade

    def setIdade(self, idade):
        """
        Modifica a idade do cliente
        Parametro:
        - idade nova do cliente
        """
        self.__idade = idade
    
    def getCpf(self):
        """
        Retorna o CPF do cliente
        """
        return self.__cpf

    def setCpf(self, cpf):
        """
        Modifica o CPF do cliente
        Parametro:
        - cpf novo do cliente
        """
        self.__cpf = cpf

    def adicionaPets(self, pet):
        if pet.getId() not in self.getPets():
            self.getPets().append(pet)

    def adicionaProdutos(self, produto):
        if produto not in self.__produtos:
            self.__produtos.append(produto)
    
    def adicionaServicos(self, servico):
        if servico not in self.__servicos:
            self.__servicos.append(servico)

    def removePets(self, pet):
        if pet in self.__pets:
            self.__pets.remove(pet)

    def removeProduto(self, produto):
        if produto in self.__produtos:
            self.__produtos.remove(produto)

    def removeServico(self, servico):
        if servico in self.__servicos:
            self.__servicos.remove(servico)
    
    def getPets(self):
        """
        Retorna a lista de pets do cliente
        """
        return self.__pets

    def getProdutos(self):
        """
        Retorna a lista de produtos do cliente
        """
        return self.__produtos

    def getServicos(self):
        """
        Retorna a lista de servicos do cliente
        """
        return self.__servicos

    def toString(self):
        print("""
        id: {}
        Cliente: {}
        Idade: {}
        CPF: {}
        Quantidade de Pets: {}
        Quantidade de Produtos: {}
        Quantidade de Servicos: {}
        """.format(self.getid(), self.getNome(), self.getIdade(), self.getCpf(), len(self.getPets()), len(self.getProdutos()), len(self.getServicos())))

    def mostraListaDePets(self):
        print(10*"-" + "Lista de Pets" + 10*"-")
        for pet in self.getPets():
            pet.toString()

    def mostraListaDeProdutos(self):
        print(10*"-" + "Lista de Produtos" + 10*"-")
        for produto in self.getProdutos():
            print (produto.toString())

    def mostraListaDeServicos(self):
        print(10*"-" + "Lista de Servicos" + 10*"-")
        for servico in self.getServicos():
            print (servico.toString())