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
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

base_censo = pd.read_csv(r'C:\Users\AMD\Downloads\census.csv')

# Dividindo em classes e previsores
base_censo_previsores = base_censo.iloc[:, 0:14].values

base_censo_classe = base_censo.iloc[:, 14].values

# transformando em numeros o que eu quero
label_encoder_workclass = LabelEncoder()
label_encoder_education = LabelEncoder()
label_encoder_relationship = LabelEncoder()
label_encoder_marital = LabelEncoder()
label_encoder_occupation = LabelEncoder()
label_encoder_race = LabelEncoder()
label_encoder_sex = LabelEncoder()
label_encoder_country = LabelEncoder()


base_censo_previsores[:, 1] = label_encoder_workclass.fit_transform(base_censo_previsores[:, 1])

base_censo_previsores[:, 3] = label_encoder_education.fit_transform(base_censo_previsores[:, 3])

base_censo_previsores[:, 5] = label_encoder_marital.fit_transform(base_censo_previsores[:, 5])

base_censo_previsores[:, 6] = label_encoder_occupation.fit_transform(base_censo_previsores[:, 6])

base_censo_previsores[:, 7] = label_encoder_relationship.fit_transform(base_censo_previsores[:, 7])

base_censo_previsores[:, 8] = label_encoder_race.fit_transform(base_censo_previsores[:, 8])

base_censo_previsores[:, 9] = label_encoder_sex.fit_transform(base_censo_previsores[:, 9])

base_censo_previsores[:, 13] = label_encoder_country.fit_transform(base_censo_previsores[:, 13])


# deixando todos valores com peso igual no one hot encoder dividindo em n colunas
base_censo_onecode = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [
                                         1, 3, 5, 6, 7, 8, 9, 13])], remainder='passthrough')

base_censo_previsores = base_censo_onecode.fit_transform(base_censo_previsores).toarray()

# escalonando
escalador = StandardScaler()
base_censo_previsores = escalador.fit_transform(base_censo_previsores)

# treinando
base_censo_previsores_treinamento, base_censo_previsores_teste, base_censo_classe_treinamento, base_censo_classe_teste=train_test_split(
    base_censo_previsores, base_censo_classe, test_size=0.15, random_state=0)

# teste
naive_bayes_teste = GaussianNB()

naive_bayes_teste = naive_bayes_teste.fit(
    base_censo_previsores_treinamento, base_censo_classe_treinamento)

previsoes = naive_bayes_teste.predict(base_censo_previsores_teste)


# comparação
accuracy_score(base_censo_classe_teste, previsoes)
