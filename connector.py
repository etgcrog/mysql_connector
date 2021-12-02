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
        return collection

    def insert_one(self, arg):
        self.connectar().insert_one(arg)
        print("Inserido com sucesso!")
        
    def insert_many(self, lista):
        # list_item = []
        # item1 = Item("Eduardo", 21).to_dict()
        # item2 = Item("Anselmo", 22).to_dict()
        # item3 = Item("James", 23).to_dict()
        
        # list_item.append(item1)
        # list_item.append(item2)
        # list_item.append(item3)
        
        # c2.insert_many(list_item)
        self.connectar().insert_many(lista)
        
    def select_one(self):
        pprint.pprint(self.connectar().find_one())
        
    def select_all(self):
        #tem que iterear para funcionar
        details = self.connectar().find()
        for n in details:
            print(n)

    def drop_collection(self):
        self.connectar().drop()
    
    

    
    
            
        