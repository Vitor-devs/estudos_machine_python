lista = []
while True:
    escolha = str(input("[i]nserir [a]pagar [l]istar [s]air")).lower()

    if escolha == "i":
        valor = str(input("O que deseja inserir? "))
        lista.append(valor)
        print(lista)

    elif escolha == "a":
        apagar = int((input("Escolha o indice para apagar ")))
        lista.pop(apagar)  # ou del lista [apagar]
        print(lista)

    elif escolha == "l":
        if lista == []:
            print("Ops a lista está vazia")
        else:
            for compra in enumerate(lista):
                print(compra)

    elif escolha == "s":
        print("A sua lista foi ", lista)
        break
