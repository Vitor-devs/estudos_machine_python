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

#Serve para caso a maioria seja definido de jeito x ao atributo de classe, se entrar um registro novo ele entra aonde está a maioria

#Importando
base_credit = Orange.data.Table(r"C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\credit_data_regras.csv")


base_credit.domain

#Pra aprender a maioria
majority = Orange.classification.MajorityLearner()

#Testar/Criar regras a maioria
previsoes = Orange.evaluation.testing.TestOnTestData(base_credit, base_credit, [majority])

#Verificar o quão bom ele foi
Orange.evaluation.CA(previsoes)


#Verificar qual é maioria
for registro in base_credit:
    print(registro.get_class())

#Ou seja a maioria é da classe 0, portanto se entrar um novo, ele classifica como 0
Counter(str(registro.get_class()) for registro in base_credit)

