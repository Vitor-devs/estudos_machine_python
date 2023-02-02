import pandas as pd

data = pd.DataFrame({
    'DATA' : ['12/12/2020', '13/12/2020', '14/12/2020', '13/12/2020', '15/12/2020', '15/12/2020'],
    'NOME' : ['THIAGO', 'THAIS', 'FILOMENA', 'CARLOS', 'JOÃO', 'CATARINA'],
    'IDADE' : [20,30,10,21,15,15],
    'ESTADO' : ['MG', 'SP', 'SP', 'RJ', 'RJ', 'SP'],
})

data['DATA'] = pd.to_datetime(data['DATA'])
data.info()