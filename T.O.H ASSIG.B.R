# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:41:11 2022

@author: lalith kumar
"""

# Test of Hypothesis of Buyer ratio between male and female in four different regions.
# Finding if male-female buyer ratio's are similar across regions.
# finding the P-VALUE(if p value is<alpha, will reject null hypothesis)

import pandas as pd
df=pd.read_csv('C:\python notes\ASSIGNMENTS\T.O.H\BuyerRatio.csv')
list(df)
df.shape
df.head()

M=50+142+131+70       # assuming male as 'M'
F=435+1523+1356+750   # assuming female as 'F'

# HISTOGRAM OF EACH REGION

df['East'].hist()
df['West'].hist()
df['North'].hist()
df['South'].hist()

#East Region
M_east=50/M
F_east=435/F
print(M_east,F_east)

import numpy as np 
count=np.array([M_east,F_east])
numb=np.array([M,F])

# applying z-test

from statsmodels.stats.proportion import proportions_ztest
stat,pvalE=proportions_ztest(count,numb)
print(stat,"\n", pvalE,"\n")

# ALPHA= 5%
alpha =0.05
'''
H0: Male and Female buying ratio is similar
H1: Male and Female buying ratio are NOT similar
'''
if pvalE>alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")

#---------------------------------------------------

#West Region

M_west=142/M
F_west=1523/F
print(M_west,F_west)

import numpy as np
count=np.array([M_west,F_west])
numb=np.array([M,F])

# applying z-test

from statsmodels.stats.proportion import proportions_ztest
stat,pvalW=proportions_ztest(count,numb)
print(stat,"\n", pvalW,"\n")

# ALPHA= 5%
alpha =0.05

'''
H0: Male and Female buying ratio is similar
H1: Male and Female buying ratio are NOT similar
'''
if pvalW>alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")

#-------------------------------------------------------

#North Region

M_north=131/M
F_north=1356/F

print(M_north,F_north)

import numpy as np
count=np.array([M_north,F_north])
numb=np.array([M,F])

#applying z-test

from statsmodels.stats.proportion import proportions_ztest
stat,pvalN=proportions_ztest(count,numb)
print(stat,"\n", pvalN,"\n")

# ALPHA=5%
alpha =0.05

'''
H0: Male and Female buying ratio is similar
H1: Male and Female buying ratio are NOT similar
'''
if pvalN>alpha:
    print("H0 is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")

#---------------------------------------------------------
#South 

M_south=70/M
F_south=750/F

print(M_south,F_south)

import numpy as np
count=np.array([M_south,F_south])
numb=np.array([M,F])

# applying z-test

from statsmodels.stats.proportion import proportions_ztest
stat,pvalS=proportions_ztest(count,numb)
print(stat,'\n',pvalS,'\n')

# ALPHA=5%
alpha =0.05

'''
H0: Male and Female buying ratio is similar
H1: Male and Female buying ratio are NOT similar
'''
if pvalS>alpha:
    print("Ho is rejected and H1 is accepted")
else:
    print("H1 is rejected and H0 is accepted")

#-----------------------------------------------------------------






























































