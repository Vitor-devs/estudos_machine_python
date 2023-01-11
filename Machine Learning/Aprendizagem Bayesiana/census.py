# Missão é prever no default se uma pessoa pode ganhar mais ou menos de 50k no default


'''

Manual 
Veja se tem numeros vazios ou sem sentido
Veja alguns dados basicos com describe
Ache os previsores e Classes
Transforme dados categóricos em numeros com LabelEnconder
Transforme os numeros obtidos em um numero que faça sentido sem peso com OneHotEncoder
Escalone os numeros com StandardScaler

'''


# importando bibliotecas
import plotly
import pandas as pd  # Manipulação de tabelas
import seaborn as sns  # Visualização de dados
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px  # Visualização de dados
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# importando base de dados
base_census = pd.read_csv(r"C:\Users\AMD\Downloads\census.csv")

# Previsor (O que vai ser usado de métrica)
x_census = base_census.iloc[:, 0:14].values

# Classe (O que queremos descobrir)
y_census = base_census.iloc[:, 14].values

# Instanciamos tudo que for categorico em um labelEncoder para poder transformar em numero e remover string
label_encoder_workclass = LabelEncoder()
label_encoder_education = LabelEncoder()
label_encoder_marital = LabelEncoder()
label_encoder_occupation = LabelEncoder()
label_encoder_relationship = LabelEncoder()
label_encoder_race = LabelEncoder()
label_encoder_sex = LabelEncoder()
label_encoder_country = LabelEncoder()

# Tudo que for string está sendo convertido em numero para a máquina ler
# iloc [linha, coluna]
x_census[:, 1] = label_encoder_workclass.fit_transform(x_census[:, 1])

x_census[:, 3] = label_encoder_education.fit_transform(x_census[:, 3])

x_census[:, 5] = label_encoder_marital.fit_transform(x_census[:, 5])

x_census[:, 6] = label_encoder_occupation.fit_transform(x_census[:, 6])

x_census[:, 7] = label_encoder_relationship.fit_transform(x_census[:, 7])

x_census[:, 8] = label_encoder_race.fit_transform(x_census[:, 8])

x_census[:, 9] = label_encoder_sex.fit_transform(x_census[:, 9])

x_census[:, 13] = label_encoder_country.fit_transform(x_census[:, 13])

# OneHotEncoder
# Balancear os pesos
# Temos varias profissões com numeros diferentes, mas não é pq pedreito é 3 e professor 4 que um é melhor que o outro, então precisamos balancear e dividir em n colunas para balancear
# coluna de profissão após o label enconder fica 1 2 3 4 5 6, então para precaver de haver mais peso em x do que y

# transformar                     "como"   "objeto"             "colunas"
base_censo_onecode = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [
                                         1, 3, 5, 6, 7, 8, 9, 13])], remainder='passthrough')  # o passthrough ele é o inplace = False do sklearn

x_census = base_censo_onecode.fit_transform(x_census).toarray()

# Escalonando
scaler_census = StandardScaler()
x_census = scaler_census.fit_transform(x_census)


# Dividindo em base de teste e base de treinamento
# cada xxx_treinamento tem que ser igual a yyy_treinamento bem como em teste
x_census_treinamento, x_census_teste, y_census_treinamento, y_census_teste = train_test_split(
    x_census, y_census, test_size=0.15, random_state=0)

# Pickle serve para salvar o arquivo que vai ser gerado | Pickle dump guarda o que você quer e o f que sai como file é o nome do arquivo que você chamou



# with open('census.pkl', mode= 'rb') as f:
#     x_census_treinamento, y_census_treinamento, x_census_teste, y_census_treinamento = pickle.load(f)


naive_credito = GaussianNB()

naive_credito = naive_credito.fit(x_census_treinamento, y_census_treinamento)


previsoes = naive_credito.predict(x_census_teste)

# Ficou baixo pq temos duas classes
accuracy_score(y_census_teste, previsoes)
