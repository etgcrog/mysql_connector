from cassandra.cluster import Cluster

cqlsh=Cluster()
keyspaces = "create KEYSPACE soulcode WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};"
session=cqlsh.connect('soulcode')

# create_table = "create table if not exists turma (id uuid primary key , nome text);"
# session.execute(create_table)

# insert_table = "insert into turma (id, nome) values (uuid(), 'eduardo')"
# session.execute(insert_table)

select_table = "select * from turma"
result = session.execute(select_table)
for i in result:
    print(i)
