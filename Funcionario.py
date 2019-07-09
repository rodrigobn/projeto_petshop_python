
class Funcionario:
    """
        Cria um funcionario.
            Parametros :
            - id.
            - nome e opcional (padrao : "").
            - senha e opcional (padrao : 0000)
        """
    def __init__(self, id = 0, nome = "", senha = 0000):
        
        self.id = id
        self.nome = nome
        self.senha = senha
    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getSenha(self):
        return self.senha
    
    def setSenha(self, senha):
        self.senha = senha