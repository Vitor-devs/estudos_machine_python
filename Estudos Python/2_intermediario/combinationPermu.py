# # Combinations, Permutations e Product - Itertools
# # Combinação - Ordem não importa - iterável + tamanho do grupo
# # Permutação - Ordem importa
# # Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product, groupby


# def print_iterator(iterator):
#     for item in iterator:
#         print(item, sep='\n')

# pessoas = [
#     'João', 'joana', 'Luiz', 'Leticia '
# ]

# camisetas = [
#     ['preta',  'branca'],
#     ['P', 'M', 'G']
# ]

# print_iterator(product(*camisetas))

# print(list(combinations(pessoas, 2)))

# #Ordem não importa (Joao, leticia) == (leticia, joao)
# for item in combinations(pessoas, 2):
#     print(item)

# #Ordem importa (Joao, leticia) != (leticia, joao)
# for item in permutations(pessoas, 2):
#     print(item)



# print_iterator(permutations(pessoas, 2))
# print_iterator(combinations(pessoas, 2))





# groupby - agrupando valores (itertools)
# Precisa estar ordenado


alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]


def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key= ordena)
grupos = groupby(alunos_agrupados, key=ordena)


for aluno in grupos:
    print(aluno)

for aluno in alunos_agrupados:
    print(aluno)