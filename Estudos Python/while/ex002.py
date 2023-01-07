nome = "Vitor Soares"

posicao = 0

novo_nome = ""
while posicao <= len(nome)-1:

    print(f'* {nome[posicao]} * ')
    novo_nome += nome[posicao]

    posicao += 1

print(novo_nome)