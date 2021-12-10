from cassandra.cluster import Cluster

class Connect:
    def __init__(self, keyspaces):
        self.keyspaces = keyspaces
        
    def get_keyspaces(self):
        return self.keyspaces
        
    def connectar(self):
        cluster = Cluster()
        session = cluster.connect(self.get_keyspaces())
        return session
    
    def fetch_all(self, table, where=''):
        if where != '':
            query = f'select * from {table} where {where}'
            result = self.connectar().execute(query)
            c = 0
            for i in result:
                print(i)
                c+=1
            print(f'Foram exibidos {c} registros')
        else:
            query = f'select * from {table}'
            result = self.connectar().execute(query)
            c = 0
            for i in result:
                print(i)
                c+=1
            print(f'Foram exibidos {c} registros')
            
    def insert(self, table, atributos_table, valores):
        query = f"INSERT INTO {table} ({atributos_table}) VALUES ({valores});"
        print(query)
        self.connectar().execute(query)
        print(f"Inserido com sucesso!")
        
            
    def create_table(self, table_name, atributos):
        query = f"CREATE TABLE {table_name} ({atributos});"
        print(query)
        self.connectar().execute(query)
        print(f'tabela {table_name} criada com sucesso')
        
if __name__ == '__main__':
    c1 = Connect(keyspaces='movie')
    c1.fetch_all('movie_table')
    
    



    
    
    