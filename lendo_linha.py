n_table_name = 0
with open('create_database.sql', 'r') as file:
    row = file.read()
    length = len(row.split('\n'))
    for i in range(length):
        table_name = (row.split('\n')[n_table_name].split(' -')[0])
        print(table_name)
        print('-' * 20)
        print(row.split('\n')[i].split(' -')[1])
        n_table_name += 1

