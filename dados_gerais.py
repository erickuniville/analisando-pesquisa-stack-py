import pandas as pd

# dataframe = pd.read_csv("teste.csv")
dataframe = pd.read_csv("survey_languages_splited.csv")

num_linguagens = len(pd.unique(dataframe.linguagem))
total_amostra = len(dataframe.values)
amostra_por_linguagem = dataframe.groupby('linguagem').size()
media_por_linguagem = dataframe.groupby('linguagem').mean()

print("Número de linguagens:    ", num_linguagens)
print("Número total de amostras:", total_amostra)
print("\nNúmero de amostra por linguagem:\n")
print(amostra_por_linguagem)
print("\nSatisfação média por linguagem:\n")
print(media_por_linguagem)
