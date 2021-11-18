from modules.connector import InterfaceDB, get_db_info

# classe com os metodos de venda
class Venda:

    def __init__(self, venda, produto, quantidade):
        try:
            self.venda = venda
            self.produto = produto
            self.quantidade = quantidade
        except Exception as e:
            print(str(e))

    def save_venda(venda, produto, quantidade):
        try:
            query = f"insert into itensvenda (venda, produto, quantidade) values ({venda}, {str(produto)}, {quantidade});"
            user, password, host, database = get_db_info()
            db = InterfaceDB(user, password, host, database)
            db.executar(query)
            print("Informacao inserida com sucesso!!!")
        except Exception as e:
            print(str(e))
            
    def listar_produto():
        try:
            user, password, host, database = get_db_info()
            db = InterfaceDB(user, password, host, database)
            alacazan = []
            venda = int(input("Informe o código da venda: "))
            while True:
                lista = []
                produto = input("Informe o código do produto: ")
                quantidade = int(input("Informe a quantidade da venda: "))
                Venda.save_venda(venda, produto, quantidade)
                lista.append(venda)
                lista.append(str(produto))
                lista.append(quantidade)
                alacazan.append(tuple(lista))
                opcao = input("Vender novo produto? S/N: ")
                if opcao in "Ss":
                    continue
                elif opcao in "Nn":
                    break
            query = "SELECT REFERENCIA, ESTOQUE FROM produtos;"
            dados2 = alacazan
            dados = db.selecionar(query)
            atualizacao=[]
            for i in range(len(dados2)):
                for j in range(len(dados)):
                    if dados2[i][1] == dados[j][0]:
                        lista=[]
                        novoestoque = dados[j][1] - dados2[i][2]
                        referencia = dados[j][0]
                        lista.append(referencia)
                        lista.append(novoestoque)
                        atualizacao.append(tuple(lista))           
            for n in atualizacao:
                query = f"UPDATE produtos SET ESTOQUE = {n[1]} WHERE REFERENCIA = {n[0]}"
                db.executar(query)
            print(atualizacao)
        except Exception as e:
            print(str(e))
    

    def deletar_produto():
        try:
            user, password, host, database = get_db_info()
            db = InterfaceDB(user, password, host, database)
            venda = int(input("Informe o código da venda que será deletado: "))
            query2 = f"SELECT PRODUTO, QUANTIDADE FROM itensvenda WHERE VENDA = {venda}"
            print(query2)
            dados2 = db.selecionar(query2)
            print(dados2)
            query = "SELECT REFERENCIA, ESTOQUE FROM produtos;"
            dados = db.selecionar(query)
            query3 = f"DELETE FROM itensvenda WHERE VENDA = {venda}"
            db.executar(query3)
            atualizacao=[]
            for i in range(len(dados2)):  
                for j in range(len(dados)):
                    if dados2[i][0] == dados[j][0]:
                        lista=[]
                        novoestoque = dados[j][1] + dados2[i][1]
                        referencia = dados[j][0]
                        lista.append(referencia)
                        lista.append(novoestoque)
                        atualizacao.append(tuple(lista))
            print(lista)
            print(atualizacao)           
            for n in atualizacao:
                query = f"UPDATE produtos SET ESTOQUE = {n[1]} WHERE REFERENCIA = {n[0]}"
                db.executar(query)
            print(atualizacao)
        except Exception as e:
            print(str(e))