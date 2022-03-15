## Medidas de Dispersão

## Desvio Médio Absoluto

import pandas as pd
import numpy as np

dados = pd.read_csv('files/dados.csv')

df = pd.DataFrame(data = {'Fulano': [8, 10, 4, 8, 6, 10, 8],
                          'Beltrano': [10, 2, 0.5, 1, 3, 9.5, 10],
                          'Sicrano': [7.5, 8, 7, 8, 8, 8.5, 7]},
                 index = ['Matemática',
                          'Português',
                          'Inglês',
                          'Geografia',
                          'História',
                          'Física',
                          'Química'])
df.rename_axis('Matérias', axis = 'columns', inplace = True)

notas_fulano = df[['Fulano']]


notas_media_fulano = notas_fulano.mean()[0]

notas_fulano['Desvio'] = notas_fulano['Fulano'] - notas_media_fulano

notas_fulano['Desvio'].sum()

notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()

notas_fulano['|Desvio|'].mean()

desvio_medio_absoluto = notas_fulano['Fulano'].mad() # No pandas
# print(desvio_medio_absoluto)

## Variância
# Variancia Populacional
# Variancia Amostral

notas_fulano['(Desvio^2'] = notas_fulano['Desvio'].pow(2)
# print(notas_fulano)

notas_fulano['(Desvio^2'].sum() / (len(notas_fulano) - 1)

variancia = notas_fulano['Fulano'].var() # No pandas
# print(variancia)

## Desvio Padrão

# print(np.sqrt(variancia))

desvio_padrao = notas_fulano['Fulano'].std()
# print(desvio_padrao)

df.mean()
df.median()
df.mode()
df.std()


# dataset = pd.DataFrame({
#     'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],
#     'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]
# })

# selecao = (dataset['Sexo'] == 'M')

# mulheres = dataset[selecao]

# print(mulheres['Idade'].std())