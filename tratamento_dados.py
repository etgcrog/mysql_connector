import pandas as pd
import numpy as np
from mysql_connector import *
from connector_cassandra import *

def importar_csv_sql():
    oldtech = Connect("root") 
    df_dados = pd.read_csv('Sistema_A_SQL.csv', sep = ',')
    df_dados = df_dados.dropna() 
    dados = np.array(df_dados)
    lista =[]                                
    for dado in dados:                   
        values = (dado[0], dado[1], dado[2])
        lista.append(values)
    values = str(lista)[1:-1]      
    # query = f"insert into vendas (nota_fiscal, nome_vendedor, total_vendas) values {values}"
    # oldtech.execute(query)
    lista_cql =[]   
    dados_sql = np.array(oldtech.execute(oldtech.select_all('vendas')))

    # df_2_cql = pd.DataFrame(dados_sql, columns=['nota_fiscal', 'nome_vendedor', 'valor_venda'])
    # print(df_2_cql)
    

def importar_csv_cql():
    oldtech = Connect("root") 
    df_dados = pd.read_csv('Sistema_B_NoSQL.csv', sep = ',')
    df_dados = df_dados.dropna() 
    df_dados.drop('nota_fiscal', axis=1, inplace=True)
    dados_numpy = np.array(df_dados)
    lista = []
    for dado in dados_numpy:                   
        values = (dado[0], dado[1])
        lista.append(values)
    print(lista)
    

        
    
        
