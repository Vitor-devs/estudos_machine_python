import plotly
import pandas as pd  # Manipulação de tabelas
import seaborn as sns  # Visualização de dados
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px  # Visualização de dados
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split


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


# Verificando aonde tem dados faltantes e somando eles em true
base_credit.isnull().sum()

# Vendo aonde eles estão
base_credit.loc[pd.isnull(base_credit['age'])]

# Substituindo o que estiver em NaN com a média, e usando o inplace para se referir ao dataframe original
base_credit['age'].fillna(base_credit['age'].mean(), inplace=True)

# Separando previsores e classes

# previsoras = x { o que vamos usar para ter bases }
# iloc ele procura via letra e coluna
# var x = base.iloc[linhas, colunas]
#    0       1       2     3     4(não entra)
# clientid income  age   loan      default
x_credit = base_credit.iloc[:, 1:4].values
x_credit

# escalonando | Selecionando todas as linhas e a primeira coluna[0]
# 0 - income | renda
# 1 - age | idade
# 2 - loan | emprestimo/divida

minimos = x_credit[:, 0].min(), x_credit[:, 1].min(), x_credit[:, 2].min()
minimos

maximos = x_credit[:, 0].max(), x_credit[:, 1].max(), x_credit[:, 2].max()
maximos
# classe = y { O que vamos concluir }
# colocamos só o 4 pq já que não tem intervalo ele vai direto
y_credit = base_credit.iloc[:, 4].values
type(y_credit)

# Como os valores oscilam muito, a idade vai de 18 a 63, e ja a divida vai de 1 até 70k, o algoritmo pode dar mais peso a divida, então precisamos normalizar isso pelo desvio padrão ou pela normalização para deixar eles na mesma escala

# Desvio padrão - indicado quando há muitos pontos de exceção (outliers)
# Normalização - indicado quando há grande amplitude
# usando standardScaler para deixar todos na mesma escala
scaler_credit = StandardScaler()
#                     |prop que padroniza| o que vai ser escalonado
x_credit = scaler_credit.fit_transform(x_credit)

# Dividindo em base de teste e base de treinamento
# "previsor treino"  "previsor teste"  "classe treino"      "classe teste"                  "previsor" "classe" "tamanho do teste" "garante que nao muda os valores"
x_credit_treinamento, x_credit_teste, y_credit_treinamento, y_credit_teste, = train_test_split(
    x_credit, y_credit, test_size=0.25, random_state=0)


# Pickle serve para salvar o arquivo que vai ser gerado | Pickle dump guarda o que você quer e o f que sai como file é o nome do arquivo que você chamou
# o mode significa como vai abrir e tudo isso vamos chamar de f
with open('credit.pkl', mode='wb') as f:
    pickle.dump([x_credit_treinamento, y_credit_treinamento,
                x_credit_teste, y_credit_teste], f)
