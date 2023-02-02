import pandas as pd

salarios = pd.read_csv(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Pandas\bases\Salaries.csv')

# Ex1- Quais colunas tem nesta base?
salarios.columns

# Ex2- Qual é a coluna de salario base?
salarios
salarios['BasePay']

# Ex3- Qual é o salário médio?
salarios['BasePay'].mean()

# Ex4- Qual é o salário máximo?
salarios['BasePay'].max()

# Ex5- Qual é o emprego do JOSEPH DRISCOLL?
salarios
cond_joseph = salarios['EmployeeName'] == 'JOSEPH DRISCOLL'
salarios[cond_joseph]['JobTitle']


# Ex6- Qual o nome da pessoa que tem o maior salário de todos?
salarios[['BasePay', 'EmployeeName']].max()

# Ex7- Qual é o salário médio por ano?
salarios
salarios.groupby('Year')['BasePay'].mean()

# Ex8- Quais são os cinco empregos mais comuns (JobTitle)?
salarios['JobTitle'].value_counts()

# Ex9- Existe correlação entre ano e salário?


# Ex10- Como criar um outro dataframe selecionando apenas algumas colunas do dataframe original?
novo_df = salarios[['EmployeeName', 'JobTitle', 'BasePay', 'Year']]



