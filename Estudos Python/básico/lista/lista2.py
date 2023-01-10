lista_a = [1,2,3]
lista_b = [4,5,6]

#Concatena sem alterar
lista_c = lista_a + lista_b
lista_c


#Ele mexe literalmente na lista a, portanto ele não retorna nada e altera o valor
lista_d = lista_a.extend(lista_b)
print(lista_d)