# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 19:45:39 2022

@author: lalith kumar
"""

# Analysing the data whether there is any difference in average TAT.
# The different laboratories at 5% significance level.

import pandas as pd

df=pd.read_csv('C:\python notes\ASSIGNMENTS\T.O.H\labTAT.csv')
df.head()
df.shape
df.describe()

#duplicate values

df[df.duplicated()].shape #(0, 4)
df[df.duplicated()]

# histogram

df['Laboratory 1'].hist()
df['Laboratory 2'].hist()
df['Laboratory 3'].hist()
df['Laboratory 4'].hist()

#oneway anova(Analysis of variance)

from scipy import stats

T_stat,P_value=stats.f_oneway(df.iloc[:,0],df.iloc[:,1],df.iloc[:,2],df.iloc[:,3])
T_stat,P_value

# Test of Hypothesis
# ALPHA 5%
alpha = 0.05

# Null Hypothesis (H0)
# Alternate Hypothesis (H1)


# H0:P_value=alpha 
# H1: P_value=!alpha

if P_value < alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")

# as per ramdom samples wiith 5% significance level there is difference in average TAT among the different laboratories.

#-------------------------------------------------------------------------------------------------------------------------


















