# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

def fatorial(num):
    fatorial = 1
    for n in range(num,0,-1):
        fatorial *= n
    return fatorial

def fat(num):
    if num <= 1:
        return 1
    return num * fat(num-1)

def recursiva(inicio = 0, fim = 10):
    if inicio >= fim:
        return fim
    inicio += 1
    return recursiva(inicio, fim)


fatorial(5)
fat(5)
recursiva()



