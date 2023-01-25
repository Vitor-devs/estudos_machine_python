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
from sklearn.metrics import accuracy_score

#Sempre verificando se possui mais de um extremo

with open(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\Pré Processamento de Dados\credit.pkl', 'rb' ) as f:
    x_credit_treinamento,y_credit_treinamento,x_credit_teste,y_credit_teste = pickle.load(f)

credit_logistic_regression = LogisticRegression(random_state= 0)

credit_logistic_regression.fit(x_credit_treinamento, y_credit_treinamento)

credit_logistic_regression.intercept_
credit_logistic_regression.coef_

previsoes = credit_logistic_regression.predict(x_credit_teste)

accuracy_score(y_credit_teste, previsoes)


