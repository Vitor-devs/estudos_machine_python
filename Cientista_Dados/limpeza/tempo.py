import pandas as pd
import statistics as sts
import seaborn as srn

baseTempo = pd.read_csv(r'C:\Users\AMD\Documents\Estudos_Machine_Python\Cientista_Dados\FormacaoCD\10.Prática em Python\dados\tempo.csv', sep=';')

baseTempo

#tratando Aparencia
sts.mode(baseTempo['Aparencia'])
baseTempo.loc[baseTempo['Aparencia'].isin(['menos']), 'Aparencia'] = 'sol'

#tratando Temperatura
baseTempo['Temperatura'].unique()

medianaTemp = sts.median(baseTempo['Temperatura'])

baseTempo.loc[(baseTempo['Temperatura'] > 130) | (baseTempo['Temperatura'] < -130), 'Temperatura'] = medianaTemp

baseTempo

#tratando Umidade
baseTempo['Umidade'].fillna(baseTempo['Umidade'].median(), inplace=True)
baseTempo.loc[baseTempo['Umidade'] > 100, 'Umidade'] = baseTempo['Umidade'].median()
baseTempo

#tratando Vento
baseTempo['Vento'].fillna(sts.mode(baseTempo['Vento']), inplace=True)
baseTempo

#tratando Jogar
# ja ta tudo ok