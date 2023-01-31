# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

def erro_b_0():
    return "Não se pode dividir por 0"

def divide(a=1,b=1):
    if not isinstance(b, (int, float)):
        try:
            a = float(a)
            b = float(b)           
            return a / b
        except ZeroDivisionError:
            return erro_b_0()
    else:
        return a/b
print(divide(2,'0'))
raise ValueError('Deu erro')
print(456)


