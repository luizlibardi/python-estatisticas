## Desvio Médio Absoluto

import pandas as pd

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
print(desvio_medio_absoluto)