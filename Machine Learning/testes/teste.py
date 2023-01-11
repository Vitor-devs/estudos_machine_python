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
from sklearn.metrics import accuracy_score

base_credito = pd.read_csv(r"C:\Users\AMD\Downloads\risco_credito.csv")

#Definindo classes e previsores
previsores_credito = base_credito.iloc[:,0:4].values
previsores_credito

classe_credito = base_credito.iloc[:,4].values
classe_credito

#transformando em numeros
label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantias = LabelEncoder()
label_encoder_renda = LabelEncoder()


previsores_credito[:,0] = label_encoder_historia.fit_transform(previsores_credito[:,0])
previsores_credito[:,1] = label_encoder_divida.fit_transform(previsores_credito[:,1])
previsores_credito[:,2] = label_encoder_garantias.fit_transform(previsores_credito[:,2])
previsores_credito[:,3] = label_encoder_renda.fit_transform(previsores_credito[:,3])

#Máquina para entender os numeros
with open('teste.pkl', 'wb') as f:
    pickle.dump([previsores_credito, classe_credito], f)

naive_bayes = GaussianNB()

naive_bayes.fit(previsores_credito, classe_credito)

previsao = naive_bayes.predict([[2,0,1,0]])
previsao

# não usamos 

