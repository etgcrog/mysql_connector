class Item:
    #Nao esquecer de fazer com args e kwargs
    def __init__(self, ):
        self.args = args 
        
    def to_dict(self):
        return {"nome":self.args, "atributos":self.kwargs}