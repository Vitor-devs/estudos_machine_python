# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

print(list(range(10)))
lista = []

# for numero in range(10):
#     lista.append(numero)
# aonde = [o que vai ser incluido 'for' o que é in 'da onde]
lista = [numero for numero in range(10)]
lista


lista_double = [numero*2 for numero in lista]
lista_double

# Mapeamento de dados em list comprehension (map)
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]


novos_produtos = [
    {**produto, 'nome': produto['nome'] + ' (01/2023)', 'preco': produto['preco']*3} # O que vai rolar
    if produto['preco'] > 20 else {**produto}                                        # Se isso acontecer
    for produto in produtos                                                          # nesses iteraveis
]


print(*novos_produtos, sep='\n')


# filtro
# novos_produtos = [{**produto, 'nome': produto['nome'], 'preco': produto['preco']*1.03}
#                   if produto['preco'] > 15 else {**produto}
#                   for produto in produtos]

#                              só inclui pares
lista = [n for n in range(10) if n % 2 == 0]
lista

novos_produtos = [{**produto, 'nome': produto['nome'], 'preco': produto['preco']*1.03}
                  if produto['preco'] > 15 else {**produto}
                  for produto in produtos]


produtos_baratos = [{**produto, 'nome' : produto['nome'], 'preco' : produto['preco']} for produto in produtos if produto['preco'] < 15]
produtos_baratos

#com mais de um for

lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))

lista = [(x,y,z) for x in range(3) for y in range(3) for z in range(2)]
lista
