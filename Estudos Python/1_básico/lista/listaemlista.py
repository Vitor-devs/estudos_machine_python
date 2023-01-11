salas= [
    #0          #1
    ['Maria', 'Joao'],              #0

    #0
    ['Pedro'],                      #1
    
    #0          #1        #2
    ["Vitor", "Soares", "Coelho"]  #2

]

sala= [['Maria', 'Joao'],['Pedro'],["Vitor", "Soares", "Coelho"]]

sala[2][3][1]

for sala in salas:
    print("A sala completa é ",sala)
    for aluno in sala:
        print(aluno)
