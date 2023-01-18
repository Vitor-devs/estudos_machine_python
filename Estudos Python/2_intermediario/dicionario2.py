# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Vitor Soares',
    'sobrenome': 'Coelho',
    'idade': 18,
}

pessoa2 = {
    'nome': 'Roger',
    'sobrenome': 'Caspian',
}

len(pessoa)

pessoa.keys()
for chave in pessoa.keys():
    print(chave)

pessoa.values()
for valor in pessoa.values():
    print(valor)

pessoa.items()
for chave, valor in pessoa.items():
    print(chave, valor)

pessoa2.setdefault('idade',15)

pessoa2.items()

pessoa.setdefault('idade', 31)

list(pessoa2)

dict(pessoa2)

d1 = {
    'c1' :'v1',
    'c2' :'v2',
    'l1' :[0,1,2],
}

#O que muda é que ambos são modificados
# Copia só o que imutavel e linka o que é mutavel (shallow copy)
# Copia tudo (deep copy)
import copy
d2 = d1.copy()
d2['l1'][0] = 15
d1

d2 = copy.deepcopy(d1)

p1 = {
    "nome" : "Vitor",
    "sobrenome" : "Coelho",
}

print(p1.get('cu'))
print(p1.get('nome'))

#Exclui do dicionario a chave tal, mas atribuindo a uma variavel vc pode guardar o valor
nome = p1.pop("nome")
print(nome)
print(p1)


#Exclui do dicionario a chave tal, mas atribuindo a uma variavel vc pode guardar o valor
ultima_chave = p1.popitem()
p1


#update ele pode criar ou atualizar items
tupla = (('tamanho da cabeça', 'cearense')),
lista = [['anime favorito', 'one piece']]
p1.update(tupla)
p1.update(lista)
p1.update({
    'nome': "ai calica",
    'vulgo': "Negro Brao"
})

p1