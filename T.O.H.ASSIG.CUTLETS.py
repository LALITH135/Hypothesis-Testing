# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 17:14:01 2022

@author: lalith kumar
"""

# Analysing the significant difference in the diameter of the cutlet between two units.
# significance level at 5%.

import pandas as pd

df=pd.read_csv('C:\python notes\ASSIGNMENTS\T.O.H\Cutlets.csv')

df.head()
df.shape
df.describe()

# HISTOGRAM

df['Unit A'].hist()
df['Unit B'].hist()

# spliting the data. 
# assume 'Unit A' as 'UA' and 'Unit B' as 'UB'

UA=pd.Series(df.iloc[:,0])
UA

UB=pd.Series(df.iloc[:,1])
UB

# Here we have two sample(Unit_A,Unit_B)
# so, by using Two tail test(ttest)
# import stats by scipy.

from scipy import stats

P_value=stats.ttest_ind(UA,UB)
P_value

P=P_value[1]

# Null Hypothesis (H0)
# Alternate Hypothesis (H1)

# H0:UA = UB
# H1:UA =!UB

# ALPHA 5% 
alpha=0.05

if P < alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")

# by analysing the randomly selected samples,there is no significant diffferent in diameter of the cutlet between two units.

#---------------------------------------------------------------------









