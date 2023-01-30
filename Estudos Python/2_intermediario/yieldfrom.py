def gen1():
    yield 1
    yield 2
    yield 3
    print('Acabou g1')

def gen2(gen):
    #Espera pelo gen1
    yield from gen
    yield from gen3()
    yield 4
    yield 6
    yield 5
    print('Acabou g2')

def gen3():
    yield 40
    yield 60
    yield 50
    print('Acabou g3')

g = gen2(gen1())


for num in g:
    print(num)