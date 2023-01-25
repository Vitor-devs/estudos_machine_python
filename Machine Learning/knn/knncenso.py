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

with open(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\Aprendizagem Bayesiana\census.pkl', 'rb') as f:
    x_census_treinamento, y_census_treinamento, x_census_teste, y_census_teste = pickle.load(f)

knncensus = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=3)

knncensus.fit(x_census_treinamento, y_census_treinamento)

previsoes = knncensus.predict(x_census_teste)


accuracy_score(y_census_teste, previsoes)



