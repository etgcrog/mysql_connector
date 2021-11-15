from numpy import random

x = random.randint(1000, size=(50,4))

with open('insertVendas.sql', 'w') as file:
    for i in x:
        file.write(str(f"{i}\n").replace('[', '(').replace(']', ')').replace(' ', ','))
    