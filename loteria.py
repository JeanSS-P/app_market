import random

lista_de_lista = []
lista = []
for _ in range(5):
    lista = []
    for i in random.sample(range(1,61),5):
        lista.append(i)
    lista.sort()
    lista_de_lista.append(lista)


print(lista_de_lista)



