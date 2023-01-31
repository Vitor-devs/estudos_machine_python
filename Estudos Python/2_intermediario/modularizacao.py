# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import modularizacao_m
try:
    import sys
    print(sys.path)
    #Procura o modulo
    sys.path.append(r"C:\Users\AMD\Documents\exemplo2.txt")
except:
    ...
print("Este módulo se chama", __name__)



