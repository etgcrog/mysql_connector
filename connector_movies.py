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

    def create_view(self, name_view, select, table_from, where):
        query_create_view = f"CREATE MATERIALIZED VIEW {name_view} AS SELECT {select} FROM {table_from} WHERE {where}"
        self.connectar().execute(query_create_view)
        print("View criada!")
           
if __name__ == '__main__':
    c1 = Connect('movie')
    # c1.create_view('movie_launch_view', 'id, title, genres_movies, launch','movie_table',
                #'id IS NOT NULL AND launch IS NOT NULL PRIMARY KEY (launch, id);')
    c1.fetch_all('movie_launch_view', where='launch = 2010')    



    
    
    