import mysql.connector
import time

class Connect:
    def __init__(self, password, user='root', database='sys', host="127.0.0.1"):
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
    
    def createDataBase(self, database):
        return f"CREATE DATABASE {database}"
    
    def createTable(self, table_name, args):
        return f"CREATE TABLE {table_name} ({args})"
        
    def dropTable(self, table_name, expression=None):
        return f"DROP TABLE {table_name}"
    
    def dropDataBase(self, table_name):
        return f"DROP SCHEMA IF EXISTS {table_name}"
    
    def describe_table(self, table):
        return f"DESCRIBE {table}" 
    
    def insert_table(self, table, features, value):
        """[USE:
        TABLE_NAME, (feature1, feature2, feature3), (values1, values2, value3)")]

        Args:
            table ([str]): [table name]
            features ([str]): [table features]
            value ([str]): [table values]
        """
        
        print(f"INSERT INTO {table}{features} VALUES ({value})") #REPARAR
        return(f"INSERT INTO {table}{features} VALUES ({value})")    
    
    def select(self, table, features, sub_selection=None, where=None):
        if where:
            print('-'*40)
            return f"SELECT {features} FROM {table} WHERE {where}"
        else:
            print('-'*16)
            return f"SELECT {features} FROM {table}"
    
    def delete(self, table, expression):
        print('DELETE FROM {table} WHERE {expression}')
        return f"DELETE FROM {table} WHERE {expression}"
    
    def openFile(self,file):
        with open(file, 'r') as file:
            row = file.read()
            return row
    
    def multiple_insertions(self, file, table, fields):
        """[MULTIPLES INSERTIONS WITH FILE PATH]

        Args:
            file ([str]]): [absolute file path]
            table ([str]): [table name]
            fields ([str]): [fields -> ex: nome_fornecedor, cnpj]
        """
    
        insertion_fornecedor = (self.openFile(file))
        diff = insertion_fornecedor.split('\n')
        for i in range(len(diff)):
            diff_stirng = str(diff[i]).replace('(','').replace(')', '')
            self.query(self.insert_table(f"{table}", f'({fields})', diff_stirng))
    
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
        [7] CREATE
        [8] DROP
        [PRESS ANY KEY FOR FOR QUIT...]
        """)
            print(f"YOU ARE ON '{self}'")
            try:
                choose = int(input("WHAT IS YOUR CHOICE: "))
                if choose == 1:
                    self.query(self.show_database())
                    print(f"YOU ARE ON {self}")
                    change = str(input("DO YOU CHANGE OF DATABASE? [Y/N]\n"))
                    if change in 'Yy':
                        db = str(input("WHICH DATABASE?\n"))
                        self.query(f"USE {db};")
                        self.set_database(db)
                        print("DATABASE CHANGED")
                    if change in 'Nn':
                        continue
                if choose == 2:
                    self.query(self.show_tables())
                if choose == 3:
                    table_describe = str(input("WHICH TABLE DO YOU WANT DESCRIBE?"))
                    self.query(self.describe_table(table_describe))
                if choose == 4:
                    try:
                        """"
                        features are separated by commas or *
                        """
                        table_selection = str(input("WHICH TABLE DO YOU WANT TO SELECT?\n"))
                        expression = str(input("TYPE THE EXPRESSION?\n"))
                        have_where = str(input("YOUR SELECT HAVE THE WHERE?[Y/N]\n"))
                        if have_where in 'Yy':
                            where = str(input("TYPE THE WHERE?\n"))
                            self.query(self.select(table_selection, expression, where=where))
                            print('-'*40)
                        if have_where in 'Nn':
                            self.query(self.select(table_selection, expression))
                            print('-'*16)
                    except Exception as erro:
                        print(erro)
                    
                if choose == 5:
                    try:
                        while True:
                            ch = int(input("DO YOU WANT TO DO ONLY INSERT[1] OR MULTIPLES[2]?\n"))
                            if ch == 1:
                                table_insertion = str(input("WHICH TABLE DO YOU WANT TO SELECT?\n"))
                                property_table = str(input("WHICH FEATURES DO YOU WANT?\n"))
                                values = str(input("WHICH VALUES?\n"))
                                self.query(self.insert_table(table_insertion, property_table, values))
                                one_more = str(input("DO YOU WANNA TO DO ONE MORE INSERT? [Y/N]\n"))
                                if one_more in 'Yy': continue
                                elif one_more in 'Nn': break
                            if ch == 2:
                                file = str(input("PASTE THE FILE PATH:\n"))
                                table_multiple = str(input("WHICH TABLE DO YOU WANT TO SELECT?\n"))
                                fields = str(input("WHICH FIELDS DO YOU WANT?\n"))
                                self.multiple_insertions(file=file, table=table_multiple, fields = fields)
                                print("DONE!")
                                break
                    except Exception as erro:
                        print(erro)
                if choose == 6:
                    try:
                        table_delete = input("WHICH TABLE DO YOU WANT SELECT?\n")
                        expression = input("PUT YOUR WHERE.. BE CAREFUL!!! \n")
                        self.query(self.delete(table_delete, expression))
                    except Exception as erro:
                        print(erro)
                if choose == 7:
                    try:
                        duo_create = int(input("DO YOU CREATE TABLE[1] OR DATABASE[2]?\n"))
                        if duo_create == 1:
                            table_name = str(input("WHICH THE TABLE NAME?\n"))
                            print("USE -> [TUPLE NAME] [INT/VARCHAR/...] [NOT NULL, PRIMARY KEY] , ...")
                            features_table = str(input("WHICH THE FEATURES?\n"))
                            self.query(self.createTable(table_name, features_table))
                    except Exception as erro:
                        print(erro)
                    if duo_create == 2:
                        try:
                            already = str(input("DO YOU HAVE ALREADY DATABASE? [Y/N]\n"))
                            if already in 'Yy':
                                name_base = str(input("WHTA WILL BE THE DATABASE NAME?\n"))
                                self.database = f'{name_base}'
                                n_table_name = 0
                                with open('create_database.sql', 'r') as file:
                                    row = file.read()
                                    length = len(row.split('\n'))
                                    for i in range(0, length):
                                        table_name = (row.split('\n')[n_table_name].split(' -')[0])
                                        self.query(self.createTable(table_name, row.split('\n')[i].split(' -')[1]))
                                        n_table_name += 1
                            if already in 'Nn':    
                                database_name = str(input("WHICH THE DATABASE NAME?\n"))
                                self.query(self.createDataBase(database_name))
                                print(f"DATABASE CREATED")
                        except Exception as erro:
                            print(erro)
                if choose == 8:
                    try:
                        data_or_table = int(input("DO YOU DROP TABLE[1] OR  DROP DATABASE[2]?\n"))
                        if data_or_table == 1:
                            table_drop_name = str(input("WHICH THE TABLE NAME?\n"))
                            self.query(self.dropTable(table_drop_name))
                            print(f"TABLE {table_drop_name} DROPPED")
                        elif data_or_table == 2:
                            data_drop_name = str(input("WHICH THE DATABASE NAME?\n"))
                            self.query(self.dropDataBase(data_drop_name))
                            print(f"DATABASE {data_drop_name} DROPPED")
                    except Exception as erro:
                        print(erro)
            except ValueError:
                print("BYE!")
                break
            
if __name__ == '__main__':
    # passwd = input("PASSWORD:\n")
    b1 = Connect("Udvf100%")
    b1.menu()                                        