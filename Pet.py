class Pet:
    """
    Cria um pet.
    Parametros :
    - id.
    - nome e opcional (padrao : "").
    - raca e opcional (padrao : "")
    - tipo e opcional (padrao : "").
    """
    def __init__(self, id, nome, raca, tipo):
        
        self.__id = id
        self.__nome = nome
        self.__raca = raca
        self.__tipo = tipo

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome
    
    def getRaca(self):
        return self.__raca
    
    def setRaca(self, raca):
        self.__raca = raca
    
    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo

    def toString(self):
        print("""
        id: {}
        Nome: {}
        Raca: {}
        Tipo: {}
        """.format(self.getId(), self.getNome(), self.getRaca(), self.getTipo()))