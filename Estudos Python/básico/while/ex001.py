qnt_linha = 5
qnt_coluna = 5

linha = 1
while linha <= qnt_linha:
    #Executado quando o while de dentro termina
    coluna = 1

    while coluna <= qnt_coluna:
        # Executado primeiro quando o de fora ja foi   
        # Ele fica aqui até terminar de executar, ou sair false    
        print(linha, coluna)
        coluna +=1
    
    linha +=1




#Continue
#Serve para que no meio do while ele exerça determinada condição e volte ao while
# contador = 0
# while contador <= 15:
    
#     contador += 1

#     if contador == 13:
#         print("Não printarei o 13")
#         continue

#     if contador >= 5 and contador<=8:
#         print("Não vou mostrar o", contador)
#         continue
    
#     print(contador)



#While
# contador = 0 
# escolha = int(input("Até qual número você quer contar?"))
# while contador < escolha:
#     contador +=1
#     print(contador)



