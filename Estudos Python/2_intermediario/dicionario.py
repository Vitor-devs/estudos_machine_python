# Dicionarios são estruturas de dados do tipo chave e valor
# Chaves são os indices
# Valor é o conteudo
# É mutável
# {} ou a palavra dict para criar um dicionário

pessoa = {
    'nome': "Vitor",
    'sobrenome': "Coelho",
    'idade': 18,
    'endereços': [
        {'rua': "Vitorio"},
        {'rua': 'Baltazar'}
    ],
    'altura': 1.69,
}

pessoa['nome']
pessoa['sobrenome']
pessoa['idade']
pessoa['endereços']

for chave in pessoa:
    print(chave, pessoa[chave], sep=" : ")

# Manipulando chave e valor
#Cria
pessoa['tamanho da cabeça em cm'] = 68

#Substitui
pessoa['nome'] = 'Maria'

#deleta um indice 
del pessoa['nome']
pessoa

#Cria dinamicamente
pe = 'tamanho_pe'
pessoa[pe] = 40

#Verifica se existe
print(pessoa.get('ultimo_nome'))