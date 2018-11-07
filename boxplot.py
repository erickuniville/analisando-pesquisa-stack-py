import matplotlib.pyplot as plt
import pandas as pd

# dataframe = pd.read_csv("teste.csv")
dataframe = pd.read_csv("job_priorities.csv")

dataframe.boxplot('satisfaction', by='priority')
plt.show()
