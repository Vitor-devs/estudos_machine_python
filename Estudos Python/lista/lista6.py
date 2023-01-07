#enumerate
lista = ["Vitor" , "Soares" , "Coelho"]

lista_enumerada = enumerate(lista)

# Ele consome o enumerate, então nao da para usar duas vezes
# Gera uma tupla
for nome in lista_enumerada:
    print(nome)


#Para contornar esse problema, pois o usa diretamente no iteravel
for nome in enumerate(lista):
    #Desempacotando
    #No indice fica os numeros e no nome o respectivo nome gerado por desempacotamento
    indice, nome = nome
    print(indice, nome)


    #OUUUUUUUUUUUUU
for indice, nome in enumerate(lista):
   print(indice, nome)   

#Ou converte para uma lista ou outra
lista_enumerada = list(enumerate(lista))
print(lista_enumerada)