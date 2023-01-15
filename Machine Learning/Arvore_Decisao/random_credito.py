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


'''
MANUAL

IMPORTA A BASE
USA PICKLE DUMP PARA A MAQUINA ENTENDER OS DADOS
CLASSIFICA A ARVORE COM DECISION TREE CLASSIFIER COM CRITERION = 'ENTROPY'
USA FIT
JA PODE IR 
'''



with open(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\Pré Processamento de Dados\credit.pkl', 'rb') as f:
    x_credit_treinamento, y_credit_treinamento, x_credit_teste, y_credit_teste = pickle.load(f)

#                                               qnt arvore
random_forest_credit = RandomForestClassifier(n_estimators= 300, criterion='entropy',random_state=0)

random_forest_credit.fit(x_credit_treinamento, y_credit_treinamento)

previsoes = random_forest_credit.predict(x_credit_teste)

accuracy_score(y_credit_teste, previsoes)