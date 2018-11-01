import pandas as pd
from scipy import stats

# dataframe = pd.read_csv("teste.csv")
dataframe = pd.read_csv("survey_languages_splited.csv")

linguagens = pd.unique(dataframe.linguagem.values)
d_data = {linguagem: dataframe['satisfacao'][dataframe.linguagem == linguagem] for linguagem in linguagens}

p_value = stats.f_oneway(d_data['C#'], d_data['Java'], d_data['JavaScript'], d_data['Kotlin'],
                         d_data['PHP'], d_data['Python'], d_data['Ruby']).pvalue

print("(Anova)   P-value:", p_value)
print("(Kruskal) P-value:", stats.kruskal(d_data['C#'], d_data['Java'], d_data['JavaScript'], d_data['Kotlin'],
                                          d_data['PHP'], d_data['Python'], d_data['Ruby']).pvalue)
