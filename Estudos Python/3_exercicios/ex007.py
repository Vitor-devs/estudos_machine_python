def executa(func, *args):
    return func(*args)

def soma(x=5, y=5):
    return x + y

def multiplica(x=10,y=10):
    return x * y

soma_com_cinco = executa(soma, 5,8)
print(soma_com_cinco)

multiplica_por_10 = executa(multiplica,5)
print(multiplica_por_10)
