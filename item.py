class Item:
    #Nao esquecer de fazer com args e kwargs
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_nome(self):
        return self.nome
        
    def get_idade(self):
        return self.idade
        
    def to_dict(self):
        return {"nome": self.get_nome(), "idade":self.get_idade()}