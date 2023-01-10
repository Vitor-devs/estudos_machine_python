import plotly
import pandas as pd  # Manipulação de tabelas
import seaborn as sns  # Visualização de dados
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px  # Visualização de dados
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


# aplicando Naive Bayes

# Bases
base_risco_credito = pd.read_csv(r"C:\Users\AMD\Downloads\risco_credito.csv")

# Dividindo Classes e Previsores

# previsores
x_credit = base_risco_credito.iloc[:, 0:4].values
x_credit

# classe
y_credit = base_risco_credito.iloc[:, 4].values
y_credit

#transformando em numeros
label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantias = LabelEncoder()
label_encoder_renda = LabelEncoder()

#Dando para cada encoder a sua respectiva planilha
x_credit[:,0] = label_encoder_historia.fit_transform(x_credit[:,0])
x_credit[:,1] = label_encoder_divida.fit_transform(x_credit[:,1])
x_credit[:,2] = label_encoder_garantias.fit_transform(x_credit[:,2])
x_credit[:,3] = label_encoder_renda.fit_transform(x_credit[:,3])

#Como a base é pequena, não usaremos OneHotEncoder

#pickle para a maquina poder ler
with open('risco_credito.pkl', 'wb') as f:
    pickle.dump([x_credit, y_credit], f)


#Usando Naive Bayes no risco crédito
# Recebe gaussianNB que é a distribuição normal
naive_risco_credito = GaussianNB()
#treinaremos ele com base na tabela de probabilidade
#                       "previsores" "classe"
naive_risco_credito.fit(x_credit, y_credit)

# história boa (0), dívida alta (0), garantias nenhuma (1), renda > 35 (2)
# história ruim (2), dívida alta (0), garantias adequada (0), renda < 15 (0)
# Com isso é retornado a classe a qual seria destinado
previsao = naive_risco_credito.predict([[2,0,1,0]])
previsao
naive_risco_credito.classes_
naive_risco_credito.class_count_
naive_risco_credito.class_prior_
