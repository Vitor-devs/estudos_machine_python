import pandas as pd
import seaborn as srn  # plotar graficos
import statistics as sts

base = pd.read_csv(
    r'C:\Users\AMD\Documents\Estudos_Machine_Python\Cientista_Dados\FormacaoCD\10.Prática em Python\dados\Churn.csv', sep=';')

base.columns = ['Id', 'Score', 'Estado', 'Genero', 'Idade', 'Patrimonio',
                'Saldo', 'Produtos', 'TemCartaoCredito', 'Ativo', 'Salario', 'Saiu']




# estados = base.groupby(['Estado']).size()
# estados.plot.bar(color='gray')

# idade = base.groupby(['Idade']).size()
# idade


# base['Idade'].describe()

