import pandas as pd

dados = pd.read_csv('./files/dados.csv')

df = pd.DataFrame(dados)

# Variaveis qualitativas ordinais - Podem ser ordenadas ou hierarquizadas
print(sorted(dados['Anos de Estudo'].unique()))

# Variaveis qualitativas nominais - Não podem ser ordenadas ou hierarquizadas
print(sorted(dados['UF'].unique()))
print(sorted(dados['Sexo'].unique()))
print(sorted(dados['Cor'].unique()))

# Variaveis quantitativas discretas - Representam uma contagem onde os valores possíveis formam um conjunto finito ou enumeravel
print(f'De {dados.Idade.min()} até {dados.Idade.max()} anos')

# Variaveis quantitativas continuas
print(f'De {dados.Altura.min()} até {dados.Altura.max()} metros')