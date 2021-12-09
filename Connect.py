from cassandra.cluster import Cluster

class Connect:
    def __init__(self, keyspace):
        self._keyspace = keyspace

    def get_keyspace(self):
        return self._keyspace
    
    def set_keyspace(self, new_key):
        self._keyspace = new_key
        
    def connectar(self):
        obj_conexao = Cluster()
        retorno_connect = obj_conexao.connect(self.get_keyspace())
        print("Conectado!!!")
        return retorno_connect
    
    def insert(self, table, atributos_table, valores,objeto_conexao):
        query = f"INSERT INTO {table} ({atributos_table}) VALUES ({valores});"
        print(query)
        objeto_conexao.execute(query)
        print(f"Inserido com sucesso!")
        
    def select_all(self, table, objeto_conexao):
        query = f'SELECT * FROM {table};'
        result = objeto_conexao.execute(query)
        for i in result: 
            print(i)
        
    def update(self, table, campo_atualizavel, id, objeto_conexao):
        query = f"UPDATE {table} SET {campo_atualizavel} WHERE {id};"
        print(query)
        objeto_conexao.execute(query)
        print('atualizado com sucesso')
        
    def delete(self, table, objeto_conexao, coluna="", where=""):
        query = f"DELETE {coluna} FROM {table} WHERE {where}"
        print(query)
        objeto_conexao.execute(query)
        print('deletado com sucesso')
    
        
    def create_table(self, table_name, atributos, objeto_conexao):
        query = f"CREATE TABLE {table_name} ({atributos});"
        print(query)
        objeto_conexao.execute(query)
        print(f'tabela {table_name} criada com sucesso')
        
    def show_table(self, objeto_conexao):
        for i in (objeto_conexao.execute('desc tables')): 
            print(i)
            
    def show_keyspaces(self, objeto_conexao):
        for i in (objeto_conexao.execute('desc keyspaces')): 
            print(i)
        
#https://community.datastax.com/questions/9667/updating-multiple-rows-in-cassandra.html
          
if __name__ == '__main__':
    c1 = Connect('soulcode')
    c1.set_keyspace('aranha')
    conectado = c1.connectar()
    c1.show_keyspaces(conectado)
    # c1.create_table('spider', "id_aranha uuid primary key, nome_do_aranha text", conectado)
    # c1.show_table(conectado)
    # c1.insert('spider', 'id_aranha, nome_do_aranha', "uuid(), 'Peter Park'", conectado)
    # c1.select_all('spider', conectado)
    # c1.insert('spider', 'id_aranha, nome_do_aranha', "uuid(), 'Wesley'", conectado)
    # c1.select_all('spider', conectado)
    
    # c1.select_all('teste2', conectado)
    # c1.insert('teste2', 'id, nome, idade', "4, 'Helder', 32", conectado)
    # c1.select_all('teste2', conectado)
    # c1.update('teste2', "nome = 'eduardo'", "idade = 23", conectado)
    # c1.select_all('teste2', conectado)
    # c1.delete('teste2', conectado, coluna='nome', where="id = 4")
    # c1.select_all('teste2', conectado)

