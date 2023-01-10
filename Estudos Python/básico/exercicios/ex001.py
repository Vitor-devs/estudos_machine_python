#Pegando e tratando o cpf
cpf = str(input("Digite seu cpf"))
cpf = cpf.split('.')
cpf = ''.join(cpf)
cpf = cpf.replace('-', '')
print(cpf)

#Somando e multiplicando
#cortando a string
cpf_soma = cpf[0:9]
cpf_soma



i = 0
listaSoma = []
for num in range(10,1,-1):
    valor = num * int(cpf_soma[i])
    i = i + 1
    listaSoma.append(valor)

resultadoSoma = 0
for numero in listaSoma:
    resultadoSoma = resultadoSoma + numero

digitoVerificador = (resultadoSoma * 10) % 11
print(f'O seu digito verificador é {digitoVerificador}')


