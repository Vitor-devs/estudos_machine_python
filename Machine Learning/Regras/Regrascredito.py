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

# importando base de dados
base_risco_credito = Orange.data.Table(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\risco_credito_regras.csv')
base_risco_credito

#Treinamento } Criação de regras
cn2 = Orange.classification.rules.CN2Learner()
regras_risco_credito = cn2(base_risco_credito)

#Acessa as regras
#Ele tenta regra a regra
for regras in regras_risco_credito.rule_list:
  print(regras)

#Não se converte para numero pois ele se guia pelas strings

base_risco_credito.domain.class_var #0 } alto     | 1  } baixo         | 2 } moderado 

previsoes = regras_risco_credito([["boa", "alta", "nenhuma", 15_35]])

#Toda previsão que você quiser fazer ele mostra aqui
for i in previsoes:
    print(base_risco_credito.domain.class_var.values[i])