lista = [123, True, "ola", 1.6, []]

for item in lista:
    print(type(item))

print(lista[2])

lista2 = [10,20,30]
#troca o que estiver na posicao 2 
lista2[2] = "tudo bem?"
print(lista2[2])

#apaga o ultimo da lista
lista2.pop() #Pode

#apaga conforme o indice que for passado
del lista2[0]
print(lista2)

#Adiciona o valor no fim
lista2.append(3.9)
print(lista2)

#Insere no index que for passado, o que for passado como segundo argumento
            #pos #o que vai ser
lista2.insert(0, "object")
print(lista2)


