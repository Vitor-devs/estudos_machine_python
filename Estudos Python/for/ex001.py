palavra = 'python'

tentativa = 0

acertos = ''

while True:
    chute = str(input("Qual a letra que você chuta que esteja na palavra mágica?"))

    if chute in palavra:
        acertos+=chute
    else: 
        print("Ops não está")
        tentativa += 1
    
    for letra in palavra:
        if letra in acertos:
            print(letra)

    

    # sair = str(input("Deseja sair? [S/N]")).upper()
    # if sair == "S" or sair[0] == "S":
    #     break
    
