#Assume Null Hypothesis Ho: No Varaince: All samples TAT population means are same
#Alternate Hypothesis Ha: It has Variance: Atleast one sample TAT population mean is different
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
df= pd.read_csv(r'C:\Users\91750\Documents\data sci\Assignment\Assignment 3\LabTAT.csv')
print(df)
p_value=stats.f_oneway(df.iloc[:,0],df.iloc[:,1],df.iloc[:,2],df.iloc[:,3])
print(p_value)
#since pvalue=2.11567 > 0.05
#We reject Ha, i.e Ho is true. Hence, All samples TAT population means are same 