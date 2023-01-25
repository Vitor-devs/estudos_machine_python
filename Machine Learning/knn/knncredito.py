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
from sklearn.neighbors import KNeighborsClassifier
import Orange
from sklearn.metrics import accuracy_score

with open(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\Pré Processamento de Dados\credit.pkl', 'rb') as f:
    x_credit_treinamento, y_credit_treinamento, x_credit_teste, y_credit_teste = pickle.load(f)


knncredit = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=3)
knncredit.fit(x_credit_treinamento, y_credit_treinamento)

previsoes = knncredit.predict(x_credit_teste)
previsoes

y_credit_teste


accuracy_score(y_credit_teste, previsoes)



