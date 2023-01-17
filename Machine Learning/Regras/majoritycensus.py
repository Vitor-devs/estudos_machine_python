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

base_census = Orange.data.Table(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\census_regras.csv')

majority = Orange.classification.MajorityLearner()


previsoes = Orange.evaluation.testing.TestOnTestData(base_census, base_census, [majority])


Orange.evaluation.CA(previsoes)

for registro in base_census:
    print(registro.get_class())

Counter(str(registro.get_class()) for registro in base_census)






