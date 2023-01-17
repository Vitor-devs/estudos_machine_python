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
base_risco_credito = Orange.data.Table(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\credit_data_regras.csv')

base_risco_credito.domain

#Dividindo em teste e treinamento

#Treinamento
#Dividindo assim ele ja separa para treinamento e teste 
#                                                 (nome da base)     (Tamanho da parte de teste)
base_dividida = Orange.evaluation.testing.sample(base_risco_credito, n = 0.25)

base_teste = base_dividida[0]
base_treinamento = base_dividida[1]

len(base_dividida[0])
len(base_dividida[1])

#Gerando as regras / treinando
cn2 = Orange.classification.rules.CN2Learner()
regras_credit = cn2(base_treinamento)

#Vendo as regras
for regras in regras_credit.rule_list:
    print(regras)

#O que queremos que ele tente adivinhar
previsoes = Orange.evaluation.testing.TestOnTestData(base_treinamento, base_teste, [lambda testdata : regras_credit])


#Verificando precisão
Orange.evaluation.CA(previsoes)
