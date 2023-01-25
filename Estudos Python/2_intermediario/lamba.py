# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordenacao(dicionario):
#     return dicionario['nome']

# lista.sort(key = ordenacao)
# lista

lista.sort(key=lambda item: item['nome'])
lista


def soma(x, y):
    return x + y


def executa(funcao, *args):
    return funcao(*args)


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# ESTRUTURA
# lambda parametro : retorno, argumento
# Não usa parenteses nem a palavra return

duplica = lambda x : x*2
duplica(2)

multiplicador = executa(
    lambda m : lambda n : n*m, 2
)

multiplicador(8)


print(
    executa(
        lambda x, y: x+y, 3,8
    ),
)

print(
    executa(
        lambda *n: sum(n), 1,8,6
    )
)