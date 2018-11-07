import pandas as pd
from scipy import stats

# dataframe = pd.read_csv("teste.csv")
dataframe = pd.read_csv("job_priorities.csv")

priotities = pd.unique(dataframe.priority.values)
d_data = {priority: dataframe['satisfaction'][dataframe.priority == priority] for priority in priotities}

p_value = stats.f_oneway(d_data['diversity'], d_data['culture'], d_data['tecnologies'], d_data['industry'],
                         d_data['departament'], d_data['financialPerf'], d_data['impactful'], d_data['profDevelopment'],
                         d_data['workFremotely'], d_data['compensations']).pvalue

print("(Anova)   P-value:", p_value)
