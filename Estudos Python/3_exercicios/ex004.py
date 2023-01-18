def duplicar(num):
    return num * 2


def triplicar(num):
    return num * 3


def quadruplicar(num):
    return num * 4


def multiplicadores(num):
    return print(f'''{num} vezes 2 é {num*2} {num} vezes 3 é {num*3} {num} vezes 4 é {num*4}''')


def criar_multiplicador(tabuada):
    def multiplicar(num):
        return num * tabuada
    return multiplicar


print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))


print(multiplicadores(15))



dobrador = criar_multiplicador(2)
triplicador = criar_multiplicador(3)
quadruplicador = criar_multiplicador(4)


print(dobrador(8))
print(triplicador(8))
print(quadruplicador(8))

