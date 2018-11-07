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

# ====================================================
# RESULTADO OUTPUT:
# ====================================================

# Número de opções de prioridade:  10
# Número total de amostras: 58965
#
# Número de amostra por prioridade:
#
# priority
# compensations       3803
# culture             2016
# departament        11428
# diversity           3939
# financialPerf       8185
# impactful           6075
# industry           10143
# profDevelopment     9269
# tecnologies         3182
# workFremotely        925
# dtype: int64
#
# Satisfação média por prioridade:
#
#
# priority          satisfaction
# compensations        4.100973
# culture              3.846726
# departament          4.042527
# diversity            4.039604
# financialPerf        4.189493
# impactful            4.010041
# industry             4.036380
# profDevelopment      3.947783
# tecnologies          4.211188
# workFremotely        4.006486
