#Desempacotamento
nomes = ["Vitor", "Soares", "Coelho"]
nome, sobrenome, sobrenome2 = nomes

nome
sobrenome
sobrenome2

#Empacotando resto com o *
dias = ['segunda', 'terca', 'quarta', 'quinta']
pior, *_ = dias
resto

# for in
lista = ['Vitor', "Soares", "Coelho"]
indice = 0
lista.append("Juan")
for nome in lista:
    print(indice, nome, sep=" = ") 
    indice += 1