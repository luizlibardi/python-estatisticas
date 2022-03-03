# Distribuição de Frequências

## Distribuição de frequências para variáveis qualitativas

from dis import dis
import pandas as pd

dados = pd.read_csv('./files/dados.csv')

# Método 1
frequencia = dados['Sexo'].value_counts()
percentual = dados['Sexo'].value_counts(normalize = True) * 100

dist_freq_qualitativas = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual})

# Renomeando os valores de indice
dist_freq_qualitativas.rename(index = {0: 'Masculino', 1: 'Feminino'}, inplace= True)

# Renomeando a coluna dos indices
dist_freq_qualitativas.rename_axis('Sexo', axis='columns', inplace=True)
print(dist_freq_qualitativas)

# Método 2 - Cruzamento das variaveis
# Tinha q ser c dicionario
freq = pd.crosstab(dados.Sexo,
                  dados.Cor)

# freq.rename(index = sexo, inplace= True)
# freq.rename(columns = cor, inplace= True)
print(freq)


perc = pd.crosstab(dados.Sexo,
                  dados.Cor) * 100

# perc.rename(index = sexo, inplace= True)
# perc.rename(columns = cor, inplace= True)
print(perc)