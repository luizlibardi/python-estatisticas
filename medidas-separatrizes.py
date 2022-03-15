# Medidas Separatrizes
import pandas as pd

## Quartis, Decis e Percentis

dados = pd.read_csv('files/dados.csv')

print(dados.Renda.quantile([i/100 for i in range(1, 100)]))


#### ==== BoxPlot ==== ####

