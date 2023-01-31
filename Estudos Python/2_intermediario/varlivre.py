# Variáveis livres + nonlocal (locals, globals)

def fora(x):
    a = x

    def dentro():
        return a
    return dentro

dentro1 = fora(1)
print(dentro1)