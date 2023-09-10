#Ho:Customer order forms defective % does not varies by centre
#Ha:Customer order forms defective % varies by centre
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency
df= pd.read_csv(r'C:\Users\91750\Documents\data sci\Assignment\Assignment 3\Costomer+OrderForm.csv')
print(df)
print(df.Phillippines.value_counts())
print(df.Indonesia.value_counts())
print(df.Malta.value_counts())
print(df.India.value_counts())
obs=np.array([[271,267,269,280],[29,33,31,20]])
print(obs)
print(chi2_contingency(obs))
#since pvalue=0.2771020991233135 > 0.05 we Accept Null Hypthesis. 
#Hence, Customer order forms defective % does not varies by centre

