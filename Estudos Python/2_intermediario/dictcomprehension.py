produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

print(produto)

for chave, valor in produto.items():
    print(chave, valor)

dc = {chave: valor.lower()
      if isinstance(valor, str) else valor
      for chave, valor in produto.items()}
dc

lista = [
    ('a', 'valor a'),
    ('b', 'valor b')
]

# ou
# dicionario = dict(lista)


dicionario = {chave: valor for chave, valor in lista}
dicionario

s1 = {2 ** i for i in range(10)}
s1
