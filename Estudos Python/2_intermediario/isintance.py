# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

lista_tipos = [str, int, bool, set, list, dict]

for item in lista:
    if isinstance(item, str):
        print('str : ', item)
    elif isinstance(item, (int, float)):
        print('int ou float:', item )
    else:
        print('outros tipos :', item)
