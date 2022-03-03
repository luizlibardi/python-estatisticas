import numpy as np

import pandas as pd

dados = pd.read_csv('./files/dados.csv')

n = dados.shape[0]

# Formula para gerar classes de acordo com a quantidade de valores no dataframe
k = 1 + (10/3) * np.log10(n)
print(int(k.round(0)))


frequencia = pd.value_counts(
    pd.cut(
        x = dados.Renda,
        bins = 17,
        include_lowest=True
    ),
    sort = False
)

percentual = pd.value_counts(
    pd.cut(
        x = dados.Renda,
        bins = 17,
        include_lowest=True
    ),
    sort = False,
    normalize = True
)

amplitude_fixa = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual})
amplitude_fixa.sort_index(ascending= False, inplace= True)
print(amplitude_fixa)