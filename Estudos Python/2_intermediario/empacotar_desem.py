a, b = 1,2
a, b = b, a

pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Souza'
}

dados_pessoa = {
    'idade' : 16,
    'altura' : 1.60
}

#Extraindo os dados de pessoa para dentro de pessoa_completa
pessoa_completa = {**pessoa, 'chave' : 'valor', **dados_pessoa}

print(pessoa_completa)

# kwargs - keyword arguments (argumentos nomeados)
def mostro_argumentos_nomeados(*args, **kwargs):
    print(f'NÃO NOMEADOS {args}')
    for chave, valor in kwargs.items():
        print(chave, valor)

#Empacotando
mostro_argumentos_nomeados('azul',1,2, nome='Joana', qlq=123)

#Desempacotando
mostro_argumentos_nomeados(**pessoa_completa)

#EX
configuracoes = {
    'arg1' : 1,
    'arg1' : 2,
    'arg3' : 3,
    'arg4' : 4,
    'arg5' : 5,
}

def mostrar_args(*args, **kwargs):
    print(f"NÃO NOMEADOS : {args}" )
    print("NOMEADOS :" )
    for chave, valor in kwargs.items():
        print(chave, valor)

mostrar_args(**configuracoes)

# Passa .values 
# Passa .keys 
# Passa .items 

# a, b = pessoa.values()
# a


# (a1,a2), b = pessoa.items()
# a1


# for chave, valor in pessoa.items():
#     print(chave, valor)