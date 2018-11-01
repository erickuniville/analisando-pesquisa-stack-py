import pandas as pd
from scipy import stats

# dataframe = pd.read_csv("teste.csv")
dataframe = pd.read_csv("survey_languages_splited.csv")

linguagens = pd.unique(dataframe.linguagem.values)
d_data = {linguagem: dataframe['satisfacao'][dataframe.linguagem == linguagem] for linguagem in linguagens}

num_linguagens = len(pd.unique(dataframe.linguagem))
total_amostra = len(dataframe.values)
amostra_por_linguagem = dataframe.groupby('linguagem').size()
media_por_linguagem = dataframe.groupby('linguagem').mean()

print("Número de linguagens:    ", num_linguagens)
print("Número total de amostras:", total_amostra)
print("\nAmostra por linguagem:\n")
print(amostra_por_linguagem)

print()
print("================================")
print("             MÉDIA              ")
print("================================")
print()

print(media_por_linguagem)

print()
print("================================")
print("             ANOVA              ")
print("================================")
print()

f_value, p_value = stats.f_oneway(d_data['C#'], d_data['Java'], d_data['JavaScript'], d_data['Kotlin'],
                                  d_data['PHP'], d_data['Python'], d_data['Ruby'])

print("ANOVA P-value:", p_value)
print("\nKruskal P-value: ", stats.kruskal(d_data['C#'], d_data['Java'], d_data['JavaScript'], d_data['Kotlin'],
                                           d_data['PHP'], d_data['Python'], d_data['Ruby']).pvalue)
