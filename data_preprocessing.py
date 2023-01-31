# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 17:42:26 2019

@author: Ammu
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df_loan=pd.read_csv("loan.csv")
print(df_loan.dtypes)
print(df_loan.head())
print(df_loan)
print(df_loan.isnull().sum())
del df_loan["Months since last delinquent"]
print(df_loan.isnull().sum())
print(df_loan)
df_loan["Annual Income"]=df_loan["Annual Income"].fillna(df_loan["Annual Income"].mean())
print(df_loan["Annual Income"].isnull().sum())
#handling outliers
#df_loan["Annual Income"].hist(bins=10)
df_loan["Annual Income_m"]=np.sqrt(df_loan["Annual Income"])
#df_loan["Annual Income_m"].hist(bins=10)
plt.boxplot(df_loan["Annual Income_m"])
plt.show()

