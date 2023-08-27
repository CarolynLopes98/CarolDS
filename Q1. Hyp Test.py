#Ho: there is no significant difference between the diameter of the cutlets between two units.
#Ha: there is significant difference between teh diameters of the cutlets in two units.
#we shall find the pvalue for Two sample Two tailed t-test
import pandas as pd
import numpy as np
df= pd.read_csv(r"C:\Users\91750\Documents\data sci\Assignment\Assignment 3\Cutlets.csv")
print(df)
A = df['Unit A'].to_numpy()
print(A)
B = df['Unit B'].to_numpy()
print(B)
from scipy import stats
p_value = stats.ttest_ind(A , B)
print(p_value)
#Since pvalue is greater than 0.05, i.e 0.47 > 0.05, hence we reject Ha, ie. we accept Ho.
#Hence, there is no significant difference between the diameter of the cutlets between two units
