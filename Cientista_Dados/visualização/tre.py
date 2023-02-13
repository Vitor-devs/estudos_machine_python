import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Cientista_Dados\FormacaoCD\13.Prática em Python\dados\trees.csv')
base
base.head()

base
altura = np.histogram(base.loc[:,"Height"], bins=6)

plt.hist(base.iloc[:, 1], bins=6)
plt.title('Arvore')
plt.ylabel('Quantidade')
plt.xlabel('Altura')

#kde = kernel density = linha de densidade
sns.histplot(base.loc[:, 'Height'], kde=True, bins=6, color='purple').set(title='Arvore')

sns.kdeplot(base.loc[:, 'Height'])

#dispersão - bom pra duas var numericas
plt.scatter(x=base.Girth, y=base.Volume)
plt.scatter(x=base.Girth, y=base.Volume, facecolors='red', marker='*')
plt.xlabel('Circuferencia')
plt.ylabel('Volume')

sns.regplot(x=base.Girth, y=base.Volume)

#x jitter evita sobreposição adicionando aleatoriedade
sns.regplot(x=base.Girth, y=base.Volume, fit_reg=False, x_jitter=0.3)


######################################
#com legenda
baseCo2 = pd.read_csv(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Cientista_Dados\FormacaoCD\13.Prática em Python\dados\co2.csv')
baseCo2

x = baseCo2['conc']
y = baseCo2['uptake']

unicos = baseCo2['Treatment'].unique()

for i in range(len(unicos)):
    indice = baseCo2['Treatment'] == unicos[i]
    plt.scatter(x[indice], y[indice], label = unicos[i])
plt.legend(loc = 'lower right')


######################################
#uma imagem com n graficos
plt.scatter(x=base.Girth, y=base.Volume)
plt.scatter(x=base.Girth, y=base.Height)
plt.scatter(x=base.Height, y=base.Volume)

plt.figure(1)
#subplot indica que vai ser mais de uma imagem
#plt.subplot(qnt_linha, qnt_coluna, posicao)

plt.subplot(2,2,1)
plt.scatter(x=base.Girth, y=base.Volume)

plt.subplot(2,2,2)
plt.scatter(x=base.Girth, y=base.Height)

plt.subplot(2,2,3)
plt.scatter(x=base.Height, y=base.Volume)

plt.subplot(2,2,4)
plt.hist(base.Height)

#################################################
#boxplot
base
#Faz o box
plt.boxplot(base['Volume'])

#Deixa na hor
plt.boxplot(base['Volume'], vert=False)

#Tira os outliers
plt.boxplot(base['Volume'], vert=False, showfliers=False)

#Faz um entalhe mostrando os quartis
plt.boxplot(base['Volume'], vert=False, showfliers=False, notch= True)


plt.boxplot(base['Volume'], vert=False, showfliers=False, notch= True, patch_artist=True)


plt.boxplot(base)
plt.boxplot(base['Volume'])
plt.boxplot(base['Girth'])


#######################################
#Barras e setores
baseInseto = pd.read_csv(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Cientista_Dados\FormacaoCD\13.Prática em Python\dados\insect.csv')

#Agrupando dados de spray e somando todas as vezes que eles aparecem, passamos o count pois ele serve de parametro de um eixo y que pode vir a ser usado (e sera)
agrupado = baseInseto.groupby(['spray'])['count'].sum()
agrupado

#Fazendo grafico de barra
agrupado.plot.bar(color='red')

agrupado.plot.bar(color=['red', 'gray', 'blue', 'green', 'pink', 'purple'])

#Gráfico de pizza
#se nao usarmos o count na linha 102 ele nao conta como parametro e é preciso passar o y=['count'] maqui
agrupado.plot.pie()

