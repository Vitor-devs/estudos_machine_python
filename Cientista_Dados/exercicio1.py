def amplitude(lista):
    lista = list(lista)
    maior = max(lista)
    menor = min(lista)
    amp = maior - menor
    return amp

lista = [1,54,5,2,7,58,5,58,6,585]
amplitude(lista)

def vertical(string):
    for letra in string:
        print(letra)

vertical('Arroz')


peso = int(input("Qual o peso da carga?"))

if peso > 10 and peso <= 20:
    print("Custa 80 mango")
elif peso > 20:
    print("Não da pra levar")
else:
    print("Custa 50tola") 
