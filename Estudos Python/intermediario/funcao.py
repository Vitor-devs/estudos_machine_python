# Função serve para replicar algo sem ficar repetindo algo
# Por padrão as funções retornam nada

def semParametro():
    return print("Fui chamado por uma função sem parâmetro")

def dobraValor(num):
    dobra = num * 2
    return dobra

def somaTres(a=0,b=0,c=0):
    soma = a + b + c
    return soma

def saudacao(nome="Dagoberto"):
    return print("Ola", nome)


print(semParametro())

print(semParametro)

print(somaTres(3,9))

#Inverte 
print(somaTres(b=3,a=9)) 
 
print(dobraValor(5))

print(saudacao())