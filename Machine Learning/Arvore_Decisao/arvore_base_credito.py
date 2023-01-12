import plotly
import pandas as pd  # Manipulação de tabelas
import seaborn as sns  # Visualização de dados
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px  # Visualização de dados
import pickle
import sklearn as sk
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix

base_credito = pd.read_csv(r"C:\Users\AMD\Downloads\credit_data.csv")
base_credito

base_credito['age'][base_credito['age'] > 0].mean()
base_credito.loc[base_credito['age'] < 0, 'age'] = 40.9277004
base_credito['age'].fillna(base_credito['age'].mean(), inplace=True)


# Separando
base_credito_previsores = base_credito.iloc[:, 1:4].values
base_credito_previsores

base_credito_classe = base_credito.iloc[:, 4].values
base_credito_classe

# Diminuindo a amplitude de valores
scaler = StandardScaler()
base_credito_previsores = scaler.fit_transform(base_credito_previsores)

# Dividindo para teste
base_credito_previsores_treinamento, base_credito_previsores_teste, base_credito_classe_treinamento, base_credito_classe_teste = train_test_split(
    base_credito_previsores, base_credito_classe, test_size=0.25, random_state=0)

# deixando a maquina ler
with open('arvore_base_credito.pkl', 'wb') as f:
    pickle.dump([base_credito_previsores_treinamento, base_credito_classe_treinamento,
                base_credito_previsores_teste,  base_credito_classe_teste], f)

# Usando a arvore
arvore_credit = DecisionTreeClassifier(criterion='entropy', random_state=0)

# Treinando
arvore_credit = arvore_credit.fit(
    base_credito_previsores_treinamento, base_credito_classe_treinamento)

# Sempre será um predict nos previsores de teste
previsoes = arvore_credit.predict(base_credito_previsores_teste)
previsoes

base_credito_classe_teste


accuracy_score(base_credito_classe_teste, previsoes)


#matriz de confusão
#A diagonal principal deve sempre ter altos numeros
cm = ConfusionMatrix(arvore_credit)
cm.fit(base_credito_previsores_treinamento, base_credito_classe_treinamento)
cm.score(base_credito_previsores_teste, base_credito_classe_teste)


previsoes = ['income', 'age', 'loan']
fig, axis = plt.subplots(nrows=1, ncols=1, figsize=(10,10))
tree.plot_tree(arvore_credit, feature_names=previsoes, class_names=['0','1'], filled=True)
