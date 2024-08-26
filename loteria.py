import random



def loteria():
    lista_de_lista = []
    lista = []
    for _ in range(5):
        lista = []
        for i in random.sample(range(1,61),5):
            lista.append(i)
        lista.sort()
        lista_de_lista.append(lista)
    print(lista_de_lista)


#Compreensão de lista
texto = "Rafael é um turmilus e esquisito."
texto_split = texto.split(" ")
a = " ".join([text.rstrip('.').lower() for text in texto_split[::-1]])
a = a.capitalize() + "."
print(a)

#modo normal


texto_reverso = texto_split[::-1]
for i in range(len(texto_reverso)):
    texto_reverso[i] = texto_reverso[i].rstrip('.').lower()
texto_reverso[0] = texto_reverso[0].capitalize()
a = " ".join(texto_reverso) + "."

print(a)






#Estou muito feliz de fazer parte dessa equipe


