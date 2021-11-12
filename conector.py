import mysql.connector

class Connect:
    def __init__(self, user, password, host, database):
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
    
    def insert_table(self, table, features, *args, **kwargs):
        return(f"INSERT INTO {table}({features}) VALUES {args}")    
        
    def select(self, table, features):
        return f"SELECT {features} FROM {table}"
    
    def menu(self):
        while True:
            print(f"""
              
        -----------------------------------DATABASE AUTOMATION--------------------------------------------
        
        [1] SHOW DATABASE
        [2] SHOW TABLES
        [3] DESCRIBE TABLES
        [4] SELECT 
        [5] INSERT
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
                table_describe = str(input("WHAT TABLE DO YOU WANT DESCRIBE?"))
                self.query(self.describe_table(table_describe))
            if choice == 4:
                """"
                features are separated by commas or *
                """
                table_selection = str(input("WHAT TABLE SELECT?\n"))
                fetaures = str(input("WHAT FEATURES?\n"))
                self.query(self.select(table_selection, fetaures))


                    
if __name__ == '__main__':
    b1 = Connect("root", "********", "127.0.0.1", "universidade")
    b1.menu()
    # b1.query(b1.insert_table("Aluno", ('nome_aluno, end_aluno, cidade_aluno, telefone_aluno'), "Maria", "Csa 3", "Vitoria", "982611454"))
    