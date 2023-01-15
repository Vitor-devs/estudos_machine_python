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
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


with open(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\Aprendizagem Bayesiana\census.pkl', 'rb') as f:
    x_census_treinamento, y_census_treinamento, x_census_teste, y_census_teste = pickle.load(f)


random_census = RandomForestClassifier(n_estimators= 90, random_state=0, criterion='entropy')

random_census.fit(x_census_treinamento, y_census_treinamento)

previsoes = random_census.predict(x_census_teste)

accuracy_score(y_census_teste, previsoes)