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

# Com  base nos dados anteriores e graficos vistos, é possível ver que existem idades negativas
# Loc serve para localizar, aqui queremos aquele com idade menor que 0
base_credit.loc[base_credit['age'] < 0]
# ou
base_credit[base_credit['age'] < 0]


# preenchendo os valores inconsistentes com as medias das idades
base_credit['age'][base_credit['age'] > 0].mean()
base_credit.loc[base_credit['age'] < 0, 'age'] = 40.9277004
base_credit[base_credit['age'] < 0]
base_credit


# Apagando só o necessario
base_credit3 = base_credit.drop(base_credit[base_credit['age'] < 0].index)
base_credit3.loc[base_credit['age'] < 0]

# apagando a coluna inteira
# axis = 1 } coluna || axis = 0 } linha
# Exclui tudo
base_credit2 = base_credit.drop('age', axis=1)
base_credit2
