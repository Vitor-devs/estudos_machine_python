import pandas as pd
import seaborn as srn  # plotar graficos
import statistics as sts

base = pd.read_csv(
    r'C:\Users\AMD\Documents\Estudos_Machine_Python\Cientista_Dados\FormacaoCD\10.Prática em Python\dados\Churn.csv', sep=';')

base.columns = ['Id', 'Score', 'Estado', 'Genero', 'Idade', 'Patrimonio',
                'Saldo', 'Produtos', 'TemCartaoCredito', 'Ativo', 'Salario', 'Saiu']

################################################# VERIFICANDO
#estados
estados = base.groupby(['Estado']).size()
estados
estados.plot.bar(color='red')

#generos
#opa, deu erro, temos os mesmos dados de maneiras diferentes
generos = base.groupby(['Genero']).size()
generos

#score
#Aparentemente nada fora do ok
srn.boxplot(base['Score']).set_title('Score')
srn.histplot(base['Score']).set_title('Score')
srn.distplot(base['Score']).set_title('Score')


#idade
#no describe tu ja ve uns coisos errados
base['Idade'].describe()
srn.boxplot(base['Idade'])
base.groupby(['Idade']).size()


#saldo
base['Saldo'].describe()
srn.histplot(base['Saldo'])
srn.distplot(base['Saldo'])


#Salario
base['Salario'].describe()
srn.boxplot(base['Salario']).set_title("Salario")
srn.distplot(base['Salario']).set_title("Salario")
base.isnull().sum()


# Conclusao:
# 'Id', - ok
# 'Score',  - ok
# 'Estado', - estados inexistentes + sp (Fora de escopo)
# 'Genero', - Mesmas informações com dados diferentes
# 'Idade', - Inconsistencias
# 'Patrimonio', - ok
# 'Saldo', - muitos zeros
# 'Salario', - nulos e muitos e muitos zeros

################################################# TRATANDO

# valores null
# tratando na e substituindo pela media
mediana = base['Salario'].median() # ou sts.median(base['Salario'])
base['Salario'].fillna(mediana, inplace=True)
base['Salario'].isnull().sum()

#genero
generos = base.groupby('Genero').size()
generos
base['Genero'].isnull().sum()

#Pq vamos substituir os na com masculino? pq ele é o que mais se repete (moda)
base['Genero'].fillna('Masculino', inplace=True)
base.isnull().sum()


#padronizando
# localiza em genero        M da col(Genero) e atribua o valor de Masculino
base.loc[base['Genero'] == 'M', 'Genero'] = 'Masculino'

#Localiza em genero   o que estiver em (F, Fem), da col Genero e substituia por Feminino
base.loc[base['Genero'].isin(['F', 'Fem']), 'Genero'] = 'Feminino'

base['Genero'].unique()
base.groupby('Genero').size()

#idade

#verificando quais são
base.loc[ (base['Idade'] < 0) | (base['Idade'] > 110)]

#pegando a mediana para por no lugar (Não usamos a média pq ela é mais sujeita a estar alterada)
idadeMediana = sts.median(base['Idade'])

#pegando os valores e setando eles como a mediana 
base.loc[ (base['Idade'] < 0) | (base['Idade'] > 110)] = idadeMediana

#ID
#tirando os duplicados
base.drop_duplicates(subset='Id', keep='first', inplace=True)
base['Id'].value_counts()


#estados
#dando o valor de RS pq ele é o que mais aparece
base.loc[base['Estado'].isin(['SP', 'TD', 'RP']), 'Estado'] = 'RS'
base.groupby('Estado').size()


#salario
#outliers
srn.boxplot(base['Salario'])
#vamos achar o desvio padrao
desv = sts.stdev(base['Salario'])
desv
#achar aqueles que são 2x maior que o desvio padrão
base.loc[base['Salario'] >= 2*desv]
#pegando a media
mediana = sts.median(base['Salario'])
#substituindo os outliers por mediana
base.loc[base['Salario'] >= 2* desv, 'Salario'] = mediana





