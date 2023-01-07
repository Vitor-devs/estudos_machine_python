import decimal
#Passa o numero como uma string
#numero_1 = decimal.Decimal('0.1')
#numero_2 = decimal.Decimal('0.7')



numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)

numero_3 = numero_1 + numero_2
print(f'{numero_3:.2f}')
#ou
print(round(numero_3,2))