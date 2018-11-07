import pandas as pd

# dataframe = pd.read_csv("teste.csv")
dataframe = pd.read_csv("job_priorities.csv")

num_opcoes = len(pd.unique(dataframe.priority))
total_amostra = len(dataframe.values)
amostra_por_prioridade = dataframe.groupby('priority').size()
media_por_prioridade = dataframe.groupby('priority').mean()

print("Número de opções de prioridade: ", num_opcoes)
print("Número total de amostras:", total_amostra)
print("\nNúmero de amostra por prioridade:\n")
print(amostra_por_prioridade)
print("\nSatisfação média por prioridade:\n")
print(media_por_prioridade)
