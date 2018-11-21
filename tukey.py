import pandas as pd

from statsmodels.stats.multicomp import MultiComparison

df = pd.read_csv("job_priorities_br.csv")

mod = MultiComparison(df['satisfaction'], df['priority'])
print(mod.tukeyhsd())
