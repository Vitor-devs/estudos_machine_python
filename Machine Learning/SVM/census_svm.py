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


with open(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\Aprendizagem Bayesiana\census.pkl', 'rb') as f:
    x_census_treinamento, y_census_treinamento, x_census_teste, y_census_teste = pickle.load(f)

svm_census = SVC(kernel='linear', random_state=0, C=3)
svm_census.fit(x_census_treinamento, y_census_treinamento)

previsoes = svm_census.predict(x_census_teste)

accuracy_score(y_census_teste, previsoes)