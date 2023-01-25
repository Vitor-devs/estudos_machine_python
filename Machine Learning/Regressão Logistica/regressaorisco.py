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
import Orange
from collections import Counter
from sklearn.linear_model import LogisticRegression

#Sempre verificando se possui mais de um extremo

with open(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\risco_credito.pkl', 'rb') as f:
    x_credit, y_credit = pickle.load(f)

x_credit
y_credit

#Vendo qual é moderado para apagar
y_credit = np.delete(y_credit, [2,7,11], axis=0)
x_credit = np.delete(x_credit, [2,7,11], axis=0)

x_credit
y_credit

#Garantindo que nao vai mudar 
logistic_risco_regression = LogisticRegression(random_state=1)

#treinando
logistic_risco_regression.fit(x_credit, y_credit)

#b0
logistic_risco_regression.intercept_

#Cada valor para cada atributo previsor
logistic_risco_regression.coef_

previsoes1 = logistic_risco_regression.predict([[0,0,1,2]])
previsoes1


