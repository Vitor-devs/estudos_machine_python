while True:
    num1 = input("Digite um número: ")
    num2 = input("Digite um segundo número: ")
    operador = input("Digite aqui seu operador: ")
    operadores_permitidos = ["+","-","*","/"]
    #print(int(num1) + operador + int(sair))

    numeros_validos = None
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        numeros_validos = True
        
    except:
        numeros_validos = None
       
    
    if numeros_validos is None:
        print("O que foi digitado não foi permitido")
        break

    if operador not in operadores_permitidos:
       print("Ops, esse operador não está disponivel")
       break

    if operador == '+':
        print(num1 + num2)
        break
    elif operador == '-':
        print(num1 - num2)
        break
    elif operador == '*':
        print(num1 * num2)
        break
    elif operador == '/':
        print(num1 / num2)
        break
    
    sair = input("Deseja sair? [S/N]: ").upper()
    if sair == "S" or sair.startswith("S"):
        break
