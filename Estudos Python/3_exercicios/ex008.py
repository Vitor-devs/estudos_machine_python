# # Exercício - Unir listas
# # Crie uma função zipper (como o zipper de roupas)
# # O trabalho dessa função será unir duas
# # listas na ordem.
# # Use todos os valores da menor lista.
# # Ex.:
# # ['Salvador', 'Ubatuba', 'Belo Horizonte']
# # ['BA', 'SP', 'MG', 'RJ']
# # Resultado
# # [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

estados = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']

for respectivo in zip(estados, siglas):
    print(respectivo)

# def zipper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return[
#         (lista1[i], lista2[i] )for i in range(intervalo_maximo)
#     ]

# print(zipper(siglas, estados))

# x = [1, 2, 3]
# y = [4, 5, 6]
# for t in zip(x, y):
#   print(t)

# print(zip(estados,siglas))


