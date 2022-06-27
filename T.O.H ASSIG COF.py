# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 21:29:48 2022

@author: lalith kumar
"""
# Telecall ueses 4 centers around the globe to process customer order forms.
# checking the defective % varies by the center by test of hypothesis. 
# data is in categorical.


import pandas as pd
df=pd.read_csv('C:\python notes\ASSIGNMENTS\T.O.H\Costomer+OrderForm.csv')

list(df)
df.head()
df.shape
df.describe()

# HISTOGRAM

df['Phillippines'].hist()
df['Indonesia'].hist()
df['Malta'].hist()
df['India'].hist()

# label encoding.
# it will Convert categorical data to numerical.

from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()
for i in range(0,4,1):
    df.iloc[:,i]=LE.fit_transform(df.iloc[:,i])
print(df)

x1=df['Phillippines']
x2=df['Indonesia']
x3=df['Malta']
x4=df['India']

# z-test

import scipy.stats as stats
z_test,pval=stats.f_oneway(x1,x2,x3,x4)
print(z_test,pval)

# Null Hypothesis (H0)
# Alternate Hypothesis (H1)

# ALPHA 5%
alpha=0.05

if pval>alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")

#--------------------------------------------------------------------------




