# higher order functions
# Função de primeira classe 
# basicamente vc pode manipular funções como achar necessário



def dentro():
    return print("estou dentro da função")

def saudacao(msg):
    dentro()
    return msg

saudacao2 = saudacao

print((saudacao("oi")))
print((saudacao2("oi")))

