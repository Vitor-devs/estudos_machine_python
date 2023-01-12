
# importando bibliotecas
import plotly
import pandas as pd  # Manipulação de tabelas
import seaborn as sns  # Visualização de dados
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px  # Visualização de dados
import pickle
import sklearn as sk
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix

# Usando pickle para importar

with open(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\Aprendizagem Bayesiana\census.pkl', 'rb') as f:
    x_census_treinamento, y_census_treinamento, x_census_teste, y_census_teste = pickle.load(
        f)


arvore_census = DecisionTreeClassifier(criterion='entropy', random_state=0)
arvore_census.fit(x_census_treinamento, y_census_treinamento)


previsoes = arvore_census.predict(x_census_teste)
previsoes

accuracy_score(y_census_teste, previsoes)


cm = ConfusionMatrix(arvore_census)
cm.fit(x_census_treinamento, y_census_treinamento)
cm.score(x_census_teste,y_census_teste)