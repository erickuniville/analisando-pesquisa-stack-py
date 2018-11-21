import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("job_priorities_br.csv")

# Agrupando pela coluna  'prioridade'
grouped = df.groupby(["priority"])
df2 = pd.DataFrame({col: vals['satisfaction'] for col, vals in grouped})

# Calculando as medianas
meds = df2.median()
meds.sort_values(ascending=False, inplace=True)
df2 = df2[meds.index]

# Plotando
df2.boxplot()

plt.show()
