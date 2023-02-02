import pandas as pd 


########################################BASECARREGADA
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

baseTeste['PRODUTO'] = 'CAMISINHA DE SABOR'
baseTeste.drop(columns='PRODUTO', inplace=True)
baseTeste

nrows, ncol = baseTeste.shape


produtos_bkp = base['PRODUTO']
baseTeste['PRODUTO'] = produtos_bkp


baseTeste['COLUNA RANDOM'] = 'Default' 

#Pois tem mais valores onde ele não é capaz de adicionar
baseTeste['Não funciona'] = [1,2,3]
baseTeste['1 a len'] = range(baseTeste.shape[0])

baseTeste['PREÇO MÉDIO REVENDA (DÓLARES)'] = baseTeste['PREÇO MÉDIO REVENDA'] * 5.07
baseTeste

novos_prod= [f'Produto {i}' for i in range(nrows)]
baseTeste['PRODUTO'] = novos_prod

elementos_lista = [f'Elemento {i}' for i in range(nrows)]
baseTeste['COLUNA A PARTIR DE LISTA'] = elementos_lista


baseTeste
baseTeste.iloc[10:16, :]
baseTeste.iloc[1,:]
baseTeste.iloc[[1,10,15,20]]
baseTeste.iloc[1,3]
baseTeste.iloc[1] 

baseTeste.loc[3:6, 'ESTADO']

baseTeste.columns
baseTeste.drop(columns=['COLUNA RANDOM', 'COLUNA A PARTIR DE LISTA'], inplace=True)
baseTeste.to_csv(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Pandas\bases\baseTestePreProcessada.csv', index=False)

#Filtrando
baseTesteLimpa = pd.read_csv((r'C:\Users\AMD\Documents\Estudos_Machine_Python\Pandas\bases\baseTestePreProcessada.csv'))
baseTesteLimpa['PRODUTO'] = produtos_bkp
baseTesteLimpa['ESTADO'].unique()
cond_sp = baseTesteLimpa['ESTADO'] == 'SAO PAULO'
postos_sp = baseTesteLimpa[cond_sp]

cond_cubico = baseTesteLimpa['UNIDADE DE MEDIDA'] ==  'R$/m3'
baseTesteLimpa[cond_cubico]

baseTesteLimpa.query('ESTADO == "SAO PAULO"')
postos_sp = baseTesteLimpa.query('ESTADO == "SAO PAULO"').reset_index(drop=True)
postos_sp.reset_index(drop=True, inplace=True)
postos_sp

#MAIS RAPIDO
cond_rj = baseTesteLimpa['ESTADO'] == 'RIO DE JANEIRO'
postos_rj = baseTesteLimpa[cond_rj]
cond_2reais = postos_rj['PREÇO MÉDIO REVENDA'] >= 2

#TAMBEM FUNFA
cond_rj = baseTesteLimpa['ESTADO'] == 'RIO DE JANEIRO'
cond_2reais = baseTesteLimpa['PREÇO MÉDIO REVENDA'] >= 2

baseTesteLimpa[cond_rj & cond_2reais]
#OUUUUUU
# | OU
# ~ NEGA
# & E 

cond_sp_rj = (baseTesteLimpa['ESTADO'] == 'SAO PAULO') | (baseTesteLimpa['ESTADO'] == 'RIO DE JANEIRO')
cond_gasosa_comum = (baseTesteLimpa['PRODUTO'] == 'GASOLINA COMUM') &  (baseTesteLimpa['PREÇO MÉDIO REVENDA'] > 2)
baseTesteLimpa[cond_sp_rj & cond_gasosa_comum]

#Não da pois ele tem caracteres especiais
baseTesteLimpa.query('ESTADO == "RIO DE JANEIRO" and PREÇO MÉDIO REVENDA > 2')

baseTesteRJ = (baseTesteLimpa['ESTADO'] == 'RIO DE JANEIRO') & (baseTesteLimpa['PREÇO MÉDIO REVENDA'] >=2)
baseTesteLimpa[baseTesteRJ].reset_index(drop=True, inplace=True)

# lista_de_anos = ['2004','2021']
# anos_desejados = baseTesteLimpa['DATA FINAL'].isin(lista_de_anos)
# baseTesteLimpa[anos_desejados] 

#verificando nulos
baseTesteLimpa.isnull().sum()

colunas_dinheiro = ['PREÇO MÉDIO REVENDA', 'PREÇO MÍNIMO REVENDA', 'PREÇO MÁXIMO REVENDA']
for item in colunas_dinheiro:
    baseTesteLimpa[item] = baseTesteLimpa[item].astype(float)
baseTesteLimpa.info()

colunas_data = ['DATA INICIAL', 'DATA FINAL']
for item in colunas_data:
    baseTesteLimpa[item] = pd.to_datetime(baseTesteLimpa[item])
baseTesteLimpa.info()
baseTesteLimpa.isnull().sum()

baseTesteLimpa.fillna(0)
base_fill = baseTesteLimpa.fillna(value={
    'PREÇO MÉDIO DISTRIBUIÇÃO ' : 10,
    'DESVIO PADRÃO DISTRIBUIÇÃO' : 20,
    'PREÇO MÍNIMO DISTRIBUIÇÃO' : 30,
    'PREÇO MÁXIMO DISTRIBUIÇÃO' : 'vazio'
})
baseTesteLimpa.dropna(inplace=False)

baseTesteLimpa.to_csv(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Pandas\bases\baseTestePreProcessadaFinal.csv', index=False)


data_final = pd.read_csv(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Pandas\bases\baseTestePreProcessadaFinal.csv')
data_final
data_final.info()
data_final.describe()['NÚMERO DE POSTOS PESQUISADOS']
data_final['NÚMERO DE POSTOS PESQUISADOS'].describe()
stats = data_final.describe()
stats.loc[['count', 'min', 'mean'], ['PREÇO MÉDIO REVENDA', 'PREÇO MÍNIMO DISTRIBUIÇÃO']]

data_final['PRODUTO'].value_counts()
data_final['PREÇO MÍNIMO DISTRIBUIÇÃO'].value_counts()


data_final['PREÇO MÉDIO REVENDA'].unique()

colunas_numericas = ['NÚMERO DE POSTOS PESQUISADOS', 'DESVIO PADRÃO REVENDA', 'COEF DE VARIAÇÃO REVENDA']

data_final['ESTADO'].value_counts().to_frame().rename(columns={'ESTADO' : 'Frequência'})



#Agrupamento 
baseTesteLimpaRegiao  = baseTesteLimpa.groupby(['REGIÃO'])
baseTesteLimpaRegiao['PREÇO MÉDIO REVENDA'].agg([min, max])
baseTesteLimpaRegiao.describe()
baseTesteLimpaRegiao.mean()
baseTesteLimpaRegiao.min()['PREÇO MÉDIO REVENDA']
baseTesteLimpaRegiao.indices
baseTesteLimpaRegiao.groups
baseTesteLimpaRegiao.get_group('SUDESTE').describe()
baseTesteLimpaRegiao.get_group('SUDESTE').isnull().sum()

baseCombReg = baseTesteLimpa.groupby(['REGIÃO', 'PRODUTO']).mean()
baseCombReg['PREÇO MÉDIO REVENDA']


#################################################DF TESTE
#apply map applymap
# apply  = funciona em dataframe e series 
# map = funciona em series
# applymap = funciona em dataframe
# axis = 1 } navegas pelas coluna
# axis = 0 } navegar pelas linha
# Sempre retorna um

def soma(linha):
    return linha.sum()

df_testes = pd.DataFrame({
    'A' : [1,2,3],
    'B' : [10,20,30],
    'C' : [100,200,300],
    'D' : [3,2,1],
},index=['Linha1', 'Linha2', 'Linha 3'])

soma(df_testes.iloc[:,0])
df_testes.apply(soma, axis=0) # assume somando as linhas
df_testes.apply(soma, axis=1) # assume somando as colunas

soma(df_testes.loc[:, 'A'])

df_testes['Média da linha'] = df_testes.apply(lambda series : series.mean(), axis=1)

df_testes['Média da coluna'] = df_testes['A'].apply(lambda x : x * 2)


df_testes['A ** 2'] = df_testes['A'].apply(lambda x : x ** 2)

nomes = pd.Series(['Vitor', 'Soares', 'Coelho'])
substituir = {'Vitor' : 'TESTE'}

nomes.replace(['Vitor'], 'TESTE')
#df[column_name].replace([old_value1, old_value2, old_value3], new_value)

#Vai indo de um em um em todas as células
df_testes.applymap(lambda x : x*2)

########################################NINJAS

#Criando um dataframe
df_ninjas = pd.DataFrame({
    'Nome' : ['Naruto', 'Sasuke', 'Sakura'],
    'Sobrenome' : ['Uzumaki', 'Uchiha', 'Haruno'],
    'Trabalho' : ['Hokage', 'Infiltrado', 'Médica'],
    'Idade' : [ 29, 30, 28],
    'Vivo' : [ True, True, True]
})


df_ninjas.sort_values(by=['Idade', 'Nome'], ascending=[False, True]).reset_index(drop=True)
df_ninjas.info()
df_ninjas.columns

for coluna in df_ninjas.columns:
    df_ninjas.rename(columns = {coluna : coluna.upper()}, inplace=True)

nomes_adicionar = []
for nomeCheio in zip(df_ninjas['NOME'].tolist(),df_ninjas['SOBRENOME'].tolist()) :
    nomes_adicionar.append(nomeCheio)

i = 0
for nome in nomes_adicionar:
    df_ninjas['NOME COMPLETO'][i] = " ".join(nome)
    i = i + 1

df_ninjas['NOME']
df_ninjas['SOBRENOME']
df_ninjas['TRABALHO']
df_ninjas['IDADE']

df_ninjas.loc['NOME COMPLETO']
df_ninjas.index

df_ninjas
#LOC localiza elementos baseado em seu nome (linha, coluna)
df_ninjas.loc[:, 'TRABALHO']

#ILOC localiza elementos baseado em seu indice (linha, coluna)
df_ninjas.iloc[:, 2]
df_ninjas.iloc[:, 0:2]

df_ninjas.index



########################################SANGUE
#Criando series
tipos_sangue = pd.Series(['O+', 'O-', 'A+', 'A-'], index=['Doador Univesal', 'Doa pouco', 'Doa para alguns', 'Sla que tipo é esse'])
tipos_sangue



########################################CONSOLE
#Mudando os nomes dos indices (Um indice para cada valor)
pesquisa_satisfação = pd.DataFrame({
    'Bom' : [10,9,8],
    'A melhorar' : [7,6,5],
    'Ruim' : [4,3,2],
    'Péssimo' : [1,0,0]
}, index=['Notas Altas', 'Notas Boas', 'Notas Ruins'])
pesquisa_satisfação
pesquisa_satisfação['Média'] = pesquisa_satisfação.mean(axis=1)

pesquisa_console = pd.DataFrame({
    'Bom' : [50,21,100],
    'Ruim' : [131,2,20],
    'Péssimo' : [30,20,1]
}, index=['Xbox One', 'Play 4', 'Switch'])
pesquisa_console
pesquisa_console.index
pesquisa_console.loc[:, ['Bom', 'Péssimo']]
pesquisa_console.loc[['Xbox One', 'Play 4'], ['Bom', 'Péssimo']]


#################################AGG
agregados = pd.DataFrame({
    'A' : [1,2,3],
    'B' : [2,3,4],
    'C' : [3,4,5]
}, index=['Linha1', 'Linha2', 'Linha 3'])

#Passa coluna a coluna ignorando nan, onde cada resultado vira uma linha
agregados.agg([sum, min])

