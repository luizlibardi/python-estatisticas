import pandas as pd

# Medidas de Tendencia Central
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

print(df)

media = (8 + 10 + 4 + 8 + 6 + 10 + 8) / 7
# print(media)
print(df.Fulano.mean())

print(dados.groupby(['Sexo'])['Renda'].mean())

# Media aritimetica -> Mais precisa

