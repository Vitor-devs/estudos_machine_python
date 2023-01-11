"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""


def escopo():
    x = 1
    print({x})


escopo()

# usando fora do escopo
print(x + x)

# Definindo variavel global


def varGlobal():
    # Mexemos na variavel n que for mais externa
    global n
    n = 10
    return n

print(n)

#args são argumentos não nomeados
# gera uma tupla
def somaInfinita(*args):
    soma = 0
    for numero in args:
        soma += numero
    return soma

def somaInfinita2(*args):
    somaFinal = sum(args)
    return somaFinal

somaInfinita2(1,2,3,4,5,6,7)

numeros = 1,2,3
somaInfinita2(*numeros)