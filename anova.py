import pandas as pd
from scipy import stats

df = pd.read_csv("job_priorities_br.csv")

priotities = pd.unique(df.priority.values)
d_data = {priority: df['satisfaction'][df.priority == priority] for priority in priotities}

p_value = stats.f_oneway(d_data['diversity'], d_data['culture'], d_data['tecnologies'], d_data['industry'],
                         d_data['departament'], d_data['financialPerf'], d_data['impactful'], d_data['profDevelop'],
                         d_data['workRemot'], d_data['compensations']).pvalue

print("(Anova)   P-value:", p_value)

