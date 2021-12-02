from pymongo import MongoClient
import pprint

class Connect:
    def __init__(self, database, collection, localhost='mongodb://127.0.0.1:27017/'):
        self.localhost = localhost
        # self.post = port
        self.database = database
        self.collection = collection
        
    def __repr__(self):
        return "BANCO {self.database} selecionado na collection {self.collection}"
        
    def connectar(self):
        client = MongoClient(self.localhost)
        db = client[self.database]
        collection = db[self.collection]
        print(f"BANCO {self.database} selecionado na collection {self.collection}")
        return collection

    def insert_one(self, arg):
        self.connectar().insert_one(arg)
        print("Inserido com sucesso!")
        
    def select_one(self):
        pprint.pprint(self.connectar().find_one())
        
    

    
    
            
        