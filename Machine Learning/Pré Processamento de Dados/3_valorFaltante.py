import plotly
import pandas as pd  # Manipulação de tabelas
import seaborn as sns  # Visualização de dados
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px  # Visualização de dados

# Importando
base_credit = pd.read_csv(r"C:\Users\AMD\Downloads\credit_data.csv")
base_credit
np.unique(base_credit['default'], return_counts=True)

# Gera grafico com base nas respostas de idade
sns.countplot(x=base_credit['default'])

# Gera um histograma com base na renda
plt.hist(x=base_credit['income'])
plt.hist(x=base_credit['loan'])

# Cria um gráfico onde se faz um x por y ou n passado no parâmetro de dimensions
# Scatter indica um grafico de dispersao, bom para ver pontos fora do padrão
# Usando a cor pelo default, deixando em evidencia quem tem default == 1, é possivel ver quem nao paga
grafico = px.scatter_matrix(base_credit, dimensions=[
                            'age', 'income', 'loan'], color=base_credit['default'])
grafico.show()

# Fazendo a correção
base_credit.loc[base_credit['age'] < 0]

# preenchendo os valores inconsistentes com as medias das idades
base_credit['age'][base_credit['age'] > 0].mean()
base_credit.loc[base_credit['age'] < 0, 'age'] = 40.9277004
base_credit[base_credit['age'] < 0]
base_credit.describe()


#Verificando aonde tem dados faltantes e somando eles em true
base_credit.isnull().sum()

#Vendo aonde eles estão
base_credit.loc[pd.isnull(base_credit['age'])]

#Substituindo o que estiver em NaN com a média, e usando o inplace para se referir ao dataframe original
base_credit['age'].fillna( base_credit['age'].mean(), inplace=True )

#Conferindo se surtiu efeito
#jeito 1
base_credit.isnull().sum()

#jeito 2 
base_credit.loc[base_credit['clientid'].isin([29,31,32])]

