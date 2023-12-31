import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2

df= pd.read_csv(r'C:\Users\91750\Documents\data sci\Assignment\Assignment 3\BuyerRatio.csv')
print(df)
table=df.iloc[:,1:6]
print(table)
value=stats.chi2(table)
print(value)
ExpectedValue = value[3]
Degree_of_freedom = 3 # (no of rows - 1) * (no. of columns -1)
chi_square=sum([(o-e)**2/e for o,e in zip(table.values,ExpectedValue)])
chi_squareStat=chi_square[0]+chi_square[1]
print(chi_squareStat)
critical_value=chi2.ppf(0.95,3)
print(critical_value)
if chi_squareStat >= critical_value:
	print('---------reject H0--------')  
else:
	print('---------fail to reject H0-------') 


