import matplotlib.pyplot as plt
import pandas as pd

# dataframe = pd.read_csv("teste.csv")
dataframe = pd.read_csv("survey_languages_splited.csv")

dataframe.boxplot('satisfacao', by='linguagem')
plt.show()
