import plotly # Manipulação de tabelas
import pandas as pd #
import seaborn as sns #Visualização de dados
import numpy as np #
import matplotlib.pyplot as plt #
import plotly.express as px #Visualização de dados

#Importando
base_credit = pd.read_csv(r"C:\Users\AMD\Downloads\credit_data.csv")
np.unique(base_credit['default'], return_counts=True)

#Gera grafico com base nas respostas de idade
sns.countplot(x = base_credit['default'])


#Gera um histograma com base na renda
plt.hist(x = base_credit['income'])
plt.hist(x = base_credit['loan'])

# Cria um gráfico onde se faz um x por y ou n passado no parâmetro de dimensions
# Scatter indica um grafico de dispersao, bom para ver pontos fora do padrão
# Usando a cor pelo default, deixando em evidencia quem tem default == 1, é possivel ver quem nao paga
grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color=base_credit['default'])
grafico.show()


