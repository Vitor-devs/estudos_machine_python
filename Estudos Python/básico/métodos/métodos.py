# split - divide uma string
# join - une a string
# strip - Corta espaços no canto da string (rstrip e lstrip)

#string zuada
frase = '      Olha só,     que coisa bacanuda'

#Como argumento vai dentro o que você quer dividir
lista_frase_cruas = frase.split(',') 
lista_frase_cruas

#Aqui vamos colocar a lista tudo ok
lista_frase = []

for i, item in enumerate(lista_frase_cruas):
    lista_frase.append(lista_frase_cruas[i].strip())

print(lista_frase)

#              como.join(o que vai ser juntado)
frases_unidas = ' '.join(lista_frase)
frases_unidas

#            como.join(o que vai ser juntado) } para cada iteravel
teste_join = '-'.join('abc')
teste_join

#pt3    como.join(o que | Iteravel)
uniao = '-'.join(lista_frase)
uniao

