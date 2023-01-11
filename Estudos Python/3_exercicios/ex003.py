def multiplica(*args):
    multiplicador = 1
    for numero in args:
        multiplicador = multiplicador * numero
    return multiplicador

def parImpar(num):
    if num % 2 == 0:
        return print("Esse numero é par")
    return print("O numero é impar")


print(multiplica(3,6,9,5,8,12,5,7))

parImpar(multiplica(5,2))


