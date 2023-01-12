import plotly
import pandas as pd  # Manipulação de tabelas
import seaborn as sns  # Visualização de dados
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px  # Visualização de dados
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

'''
MANUAL

IMPORTA A BASE
USA PICKLE DUMP PARA A MAQUINA ENTENDER OS DADOS
CLASSIFICA A ARVORE COM DECISION TREE CLASSIFIER COM CRITERION = 'ENTROPY'
USA FIT
JA PODE IR 
'''



#Importando as bases de dados
base_credit = pd.read_csv(r"C:\Users\AMD\Downloads\credit_data.csv")
base_credit

#Nesse arquivo já estão salvos os arquivos previsores e de classe

# x_credit = ja foi usado o label encoder dos previsores
# y_credit = os atributos de classe

with open(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Machine Learning\risco_credito.pkl', 'rb') as f:
    x_credit, y_credit = pickle.load(f)

arvore_risco_credito = DecisionTreeClassifier(criterion='entropy')

#Fit ele encaixa os dados da maneira que estamos trabalhando, por isso usamos o fit depois de definir se vamos trabalhar com Naive Bayes, Arvore, redes Neurais e etc

#o que vamos encaixar.fit(previsores, classe)
arvore_risco_credito.fit(x_credit, y_credit)

#Retorna o grau de importancia de cada previsor 
#credito, divida, garantia, renda
arvore_risco_credito.feature_importances_

#pltoando em um grafico

arvore_risco_credito.classes_
previsores = ['historia', 'dívida', 'garantias', 'renda']
figura,eixos = plt.subplots(nrows=1, ncols=1, figsize = (10,10))
tree.plot_tree(arvore_risco_credito, feature_names=previsores, class_names=arvore_risco_credito.classes_, filled=True)


teste = arvore_risco_credito.predict([[0,0,1,1]])
teste
