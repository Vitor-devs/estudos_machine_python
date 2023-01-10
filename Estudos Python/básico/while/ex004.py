frase = 'O python é uma linguagem de programação multiparadigma, criado por Guido van Rossum'

# for letra in frase:
#     print("A letra", letra, "Apareceu ",frase.count(letra), "vezes")
    

i = 0
qtd = 0
letra = ''

while i < len((frase)):

    letra_atual = frase[i]

    if letra_atual == ' ':
        i+=1
        continue

    qtd_maior = frase.count(letra_atual)
    print("A letra", letra_atual, "Apareceu ", frase.count(letra_atual), "vezes")

    if qtd < qtd_maior:
        qtd = qtd_maior
        letra = letra_atual
        
    i += 1
print("A letra que apareceu mais vezes foi:",letra ,"\n", "Com ",qtd, "vezes")