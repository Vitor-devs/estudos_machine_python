from functools import partial
from types import GeneratorType
from functools import reduce

def print_iterator(iteravel):
    for item in iteravel:
        print(item)


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

#List comprehension
novos_prod = [
    p for p in produtos
    if p['preco'] > 20
]

#Funcional
novos_prod_filter = filter(
    lambda p : p['preco'] > 10, produtos
)

total = 0 
for p in produtos:
    total = total + p['preco']

total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)


print_iterator(novos_prod_filter)


print_iterator(produtos)

novos_prod = [{**p, 'preco' : p['preco']*2} for p in produtos]



#Mapeia e recebe uma função para isso
def dobra_preco_produto(produto):
    return {**produto, produto['preco'] : produto['preco'] * 2}
novos_prod = map(dobra_preco_produto, produtos)

print_iterator(novos_prod)

print_iterator(
    map(
        lambda x : f'Posição de número: {x}',
        [1,2,3]
    )
)