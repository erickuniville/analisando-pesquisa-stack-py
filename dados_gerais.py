import pandas as pd

df = pd.read_csv("job_priorities_br.csv")

num_opcoes = len(pd.unique(df.priority))
total_amostra = len(df.values)
amostra_por_prioridade = df.groupby('priority').size()
media_por_prioridade = df.groupby('priority').mean()

print("Número de opções de prioridade: ", num_opcoes)
print("Número total de amostras:", total_amostra)
print("\nNúmero de amostra por prioridade:\n")
print(amostra_por_prioridade)
print("\nSatisfação média por prioridade:\n")
print(media_por_prioridade)

# OUTPUT RESULTADOS
# Número de opções de prioridade:  10
# Número total de amostras: 1517
#
# Número de amostra por prioridade:
#
# priority
# compensations     94
# culture           44
# departament      243
# diversity         77
# financialPerf    229
# impactful        212
# industry         199
# profDevelop      350
# tecnologies       40
# workRemot         29
# dtype: int64
#
# Satisfação média por prioridade:
#
#                satisfaction
# priority
# compensations      4.010638
# culture            3.454545
# departament        3.777778
# diversity          4.116883
# financialPerf      3.781659
# impactful          4.051887
# industry           3.708543
# profDevelop        3.674286
# tecnologies        3.450000
# workRemot          3.862069
