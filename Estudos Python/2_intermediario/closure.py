'''
Closure -
Função dentro de uma função onde uma depêndencia que existe é resolvida de dentro pra fora com passo a passo onde há certa autonomia de cada argumento
'''

def criarSaudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criarSaudacao("bom dia")
falar_boa_tarde = criarSaudacao("Boa tarde")

falar_bom_dia("Vitor")
falar_boa_tarde("jubileu")

for nome in ['vitor', 'soares', 'cu']:
    print(falar_bom_dia(nome))