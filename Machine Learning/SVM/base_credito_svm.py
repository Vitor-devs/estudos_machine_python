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
from sklearn.svm import SVC

with open(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\Pré Processamento de Dados\credit.pkl', 'rb') as f:
    x_credit_treinamento, y_credit_treinamento, x_credit_teste, y_credit_teste = pickle.load(f)

#              dimensionalidade | mudança nos dados | testes
svm_credit = SVC(kernel='rbf', random_state = 0 , C=15)

svm_credit.fit(x_credit_treinamento, y_credit_treinamento)

previsoes = svm_credit.predict(x_credit_teste)

accuracy_score(y_credit_teste, previsoes)


