import pandas as pd 
tsv_file='2004-2021.tsv'
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('2004-2021.csv',index=False)

base = pd.read_csv(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Pandas\bases\2004-2021.csv')

base.isnull().sum()
base.describe()
base.info()
base.shape[0] #linhas
base.shape[1] #colunas
base.columns

base.iloc[0:0]

baseTeste = base.copy()
cond_sudeste = base['REGIÃO'] == "SUDESTE"
baseSudeste = baseTeste[cond_sudeste]

base['REGIÃO']
base
#iloc  linha,coluna
base.iloc[:,1]

base['REGIÃO'].value_counts()
















#Criando um dataframe
df_ninjas = pd.DataFrame({
    'Nome' : ['Naruto', 'Sasuke', 'Sakura'],
    'Sobrenome' : ['Uzumaki', 'Uchiha', 'Haruno'],
    'Trabalho' : ['Hokage', 'Infiltrado', 'Médica'],
    'Idade' : [ 29, 30, 28],
    'Vivo' : [ True, True, True]
})

df_ninjas.info()
df_ninjas.columns

for coluna in df_ninjas.columns:
    df_ninjas.rename(columns = {coluna : coluna.upper()}, inplace=True)

df_ninjas['NOME']
df_ninjas['SOBRENOME']
df_ninjas['TRABALHO']
df_ninjas['IDADE']

#Criando series
tipos_sangue = pd.Series(['O+', 'O-', 'A+', 'A-'], index=['Doador Univesal', 'Doa pouco', 'Doa para alguns', 'Sla que tipo é esse'])
tipos_sangue


