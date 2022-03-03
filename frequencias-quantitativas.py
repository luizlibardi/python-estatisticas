import pandas as pd

dados = pd.read_csv('./files/dados.csv')

print(dados.Renda.min())
print(dados.Renda.max())

classes = [0, 1576, 3152, 7880, 15760, 200000]
labels = ['E', 'D', 'C', 'B', 'A']

# Criar tabela de frequências

frequencia = pd.value_counts(pd.cut(x = dados.Renda,
       bins = classes,
       labels = labels,
       include_lowest= True))

percentual = pd.value_counts(pd.cut(x = dados.Renda,
       bins = classes,
       labels = labels,
       include_lowest= True),
       normalize= True)
   
dist_freq_quantitativas_personalizadas = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual})
dist_freq_quantitativas_personalizadas.sort_index(ascending= False, inplace= True)
print(dist_freq_quantitativas_personalizadas)