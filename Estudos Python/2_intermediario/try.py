# try e except para tratar exceções
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    a = 18 
    b = 0
    c = a/b

except ZeroDivisionError:
    print("ops, não é possível dividir")
except NameError:
    print("Alguma das variaveis não está definida")
except ( IndentationError) as error:
    print('Erro Desconhecido/Identação : ',error)


try:
    print(1)
# Pode usar qnts excepts vc quiser
except:
    print(2)
else:
    print('Sem erro')
finally: #Sempre será executado
    print(3)
