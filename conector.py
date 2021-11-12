import mysql.connector
import time
import os

class Connect:
    def __init__(self, user, password, database, host="127.0.0.1"):
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
    
    def query(self, query):
        try:
            cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)
            cursor = cnx.cursor()
            cursor.execute(query)
            for row in cursor:
                print(str(row))
            cursor.close()
            cnx.commit()
        except Exception as e:
            print(str(e))
        finally:
            cnx.close()
      
    def show_database(self):
        print("<<<<<<<<<<<<<<<<<<<<< DATABASES >>>>>>>>>>>>>>>>>>>>>.")
        return "SHOW DATABASES"
    
    def show_tables(self):
        print("<<<<<<<<<<<<<<<<<<<<< TABLES >>>>>>>>>>>>>>>>>>>>>.")
        return f"SHOW TABLES"
        
    def describe_table(self, table):
        return f"DESCRIBE {table}" 
    
    def insert_table(self, table, features, value):
        print(f"INSERT INTO {table}({features}) VALUES ({value})")
        return(f"INSERT INTO {table}({features}) VALUES ({value})")    
        
    def select(self, table, features):
        return f"SELECT {features} FROM {table}"
    
    def delete(self, table, expression):
        return f"DELETE FROM {table} WHERE {expression}"
    
    def menu(self):
        while True:
            time.sleep(1)

            print(f"""
              
        -----------------------------------DATABASE AUTOMATION--------------------------------------------
        
        [1] SHOW DATABASE
        [2] SHOW TABLES
        [3] DESCRIBE TABLES
        [4] SELECT 
        [5] INSERT
        [6] DELETE
        [9] SAIR
        """)
            print(f"YOU ARE ON '{self}'")
            choice = int(input("WHAT IS YOUR CHOICE:"))
            
            if choice == 1:
                self.query(self.show_database())
                print(f"YOU ARE ON {self.get_database}")
                change = str(input("DO YOU CHANGE OF DATABASE? [Y/N]\n"))
                if change in 'Yy':
                    db = str(input("WHICH DATABASE?\n"))
                    self.query(f"USE {db};")
                    self.set_database(db)
                    print("DATABASE CHANGED")
                if change in 'Nn':
                    continue
            if choice == 2:
                self.query(self.show_tables())
            if choice == 3:
                table_describe = str(input("WHICH TABLE DO YOU WANT DESCRIBE?"))
                self.query(self.describe_table(table_describe))
            if choice == 4:
                """"
                features are separated by commas or *
                """
                table_selection = str(input("WHICH TABLE DO YOU WANT TO SELECT?\n"))
                fetaures = str(input("WHAT FEATURES?\n"))
                self.query(self.select(table_selection, fetaures))
                
            if choice == 5:
                while True:
                    ch = int(input("DO YOU WANT TO DO ONLY SELECT[1] OR MULTIPLES[2]?\n"))
                    if ch == 1:
                        table_insertion = str(input("WHICH TABLE DO YOU WANT TO SELECT?\n"))
                        property_table = str(input("WHICH FEATURES DO YOU WANT?\n"))
                        values = str(input("WHICH VALUES?\n"))
                        b1.query(b1.insert_table(table_insertion, property_table, values))
                    if ch == 2:
                        file = str(input("PASTE THE FILE PATH:\n"))
                        self.multiple_insertions(file=file)
                        print("DONE!")
                        break                
            if choice == 6:
                table_delete = input("WHICH TABLE DO YOU WANT SELECT?\n")
                expression = input("PUT YOUR WHERE.. BE CAREFUL!!! \n")
                self.query(self.delete(table_delete, expression))
                
            if choice == 9:
                break
            
    def openFile(self,file):
        with open(file, 'r') as file:
            row = file.read()
            return row
        
    def multiple_insertions(self, file):
        """[HOW TO]
            FILE FORMAT =  (" ", " ", ...)
        Args:
            file ([string]): [absolute path file]
        """
        insertion_fornecedor = (self.openFile(file))
        diff = insertion_fornecedor.split('\n')
        for i in range(len(diff)):
            diff_stirng = str(diff[i]).replace('(','').replace(')', '')
            self.query(self.insert_table("Fornecedor", ('nome_fornecedor, cnpj'), diff_stirng))
        
                        
if __name__ == '__main__':
    b1 = Connect("root", 'Udvf100%', "Produtos")
    b1.menu()
    
                
    # b1.query(b1.select('Fornecedor', '*'))