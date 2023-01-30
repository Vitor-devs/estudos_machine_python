iteravel = ['Eu', 'Tenho', '__iter__']

#Ele(iterator) só é responsável por te entregar o valor atual e o próximo, mas ele não sabe nada sobre o iteravel
iterator = iter(iteravel) #iter tem __next__
iterator


#generator
#funções que sabem pausar

def fatorial(num):
    for i in range(num):
        if i > 0:
            num = num * i
            fat = num
    return num
print(fatorial(3))


itens = ['arroz', 'feijao']
['item : ' + item for item in itens ]    
