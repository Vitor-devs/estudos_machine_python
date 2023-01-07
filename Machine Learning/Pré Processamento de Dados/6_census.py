#Missão é prever no default se uma pessoa pode ganhar mais ou menos de 50k no default

#importando bibliotecas
import plotly
import pandas as pd  # Manipulação de tabelas
import seaborn as sns  # Visualização de dados
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px  # Visualização de dados
from sklearn.preprocessing import StandardScaler

#importando base de dados
base_census = pd.read_csv(r"C:\Users\AMD\Downloads\census.csv")
base_census.describe()

plt.hist(x = base_census['age'])

grafico = px.scatter_matrix(base_census, dimensions=['age', 'education'])
grafico.show()