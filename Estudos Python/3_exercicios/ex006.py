import copy
# copy, sorted, produtos.sort
# Exercícios
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumente os preços dos produtos a seguir em 10%
for produto in produtos:
    produto['preco'] = round(produto['preco'] * 1.10, 2)


# Gere novos_produtos por deep copy (cópia profunda)
lista_produtos = copy.deepcopy(produtos)
lista_produtos.append({'nome' : 'produto AINAIN', 'preco' : 32})


# Ordene os produtos por nome decrescente (do maior para menor)
ordenado_nome = sorted(lista_produtos, key= lambda p : p['nome'])
ordenado_nome



# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
deeper_nome = copy.deepcopy(produtos)
deeper_nome_ordenado = sorted(deeper_nome, key = lambda p : p['nome'])

# Ordene os produtos por preco crescente (do menor para maior)
inverso_preco = lista_produtos.copy()
inverso_preco = sorted(lista_produtos, key= lambda p: p['preco'])

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
deeper_preco = copy.deepcopy(produtos)
deeper_preco_ordenado = sorted(deeper_preco, key = lambda p : p['preco'])