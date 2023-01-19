import random


perguntas = [
    {
        "pergunta" : "Quanto é 2 + 2?",
        "alternativa" : ['2', '3', '4', '5'],
        "resposta" : "3",
    },
    {
        "pergunta" : "Protagonista de One Piece?",
        "alternativa" : ["Luffy", "Zoro", "Sanji", "Ace"],
        "resposta" : "2",
    },
]

acertos = 0

while True:
    x = random.randint(0,len(perguntas)-1)

    pergunta = perguntas[random.randint(0,len(perguntas)-1)]

    print(perguntas[x]['pergunta'])

    i = 0
    for item in perguntas[x]['alternativa']:
        i = i + 1
        print(f'Alternativa {i}-) {item}')

    resposta = str(input("Qual a resposta? "))

    if resposta == perguntas[x]['resposta']:
        print("Acertou")
        acertos = acertos + 1
    else: 
        print("Você errou a alternativa certa era: ",perguntas[x]['resposta'])
    
    sair = str(input("Quer sair? [s]im [n]ão"))

    if sair == "s":
        print("Vcê acertou: ", acertos)
        break
    else:
        continue