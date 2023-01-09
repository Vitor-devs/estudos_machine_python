# Missão é prever no default se uma pessoa pode ganhar mais ou menos de 50k no default

# importando bibliotecas
import plotly
import pandas as pd  # Manipulação de tabelas
import seaborn as sns  # Visualização de dados
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px  # Visualização de dados
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# importando base de dados
base_census = pd.read_csv(r"C:\Users\AMD\Downloads\census.csv")


x_census = base_census.iloc[:,0:14].values
x_census

y_census = base_census.iloc[:,14].values
y_census



