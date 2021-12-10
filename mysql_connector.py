import mysql.connector

import time

class Connect:
    def __init__(self, password, user='root', database='OLDTECH', host="172.17.0.4"):
        """[summary]
        Args:
            user ([str]): [User to connect in database]
            password ([str]): [Password to connect in database]
            database ([str]): [DataBase's name]
            host ([str]): [ip to connect in database, default = localhost]
        """
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        
    def __str__(self) -> str:
        return  self.database
    
    def get_database(self):
        return self.database
    
    def set_database(self, database):
        self.database = database
        
    def execute(self, funciton):
        try:
            cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.get_database())
            cursor = cnx.cursor()
            cursor.execute(funciton)
            print(cursor.fetchall())
            cnx.commit()
            cursor.close()
        except Exception as e:
            print(str(e))
        finally:
            cnx.close()
            
    def select_all(self, table):
        return f"SELECT * FROM {table}"
    
            
if __name__ == '__main__':
    c1 = Connect('root')
    c1.query('select * from vendas')