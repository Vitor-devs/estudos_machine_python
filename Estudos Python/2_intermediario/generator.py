# Introdução às Generator functions em Python
# São funções que sabem pausar
# generator = (n for n in range(1000000))

def generator(n=0, maximo=10):
    while True:
        yield n 

        if n == maximo:
            return 
            
        n += 1 
        

gen = generator()


print(next(gen)) # Passa do primeiro yield e printa o continuando
print(next(gen)) # Passa o segundo yield
print(next(gen)) # Passa o terceiro

for n in gen:
    print(n)