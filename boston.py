# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:10:05 2019

@author: Unitech
"""
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats

diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())
#eliminaqte the variable of values p>0.5 & find the accuracy
est3 = sm.OLS(y, X2[["zn","indus","chas","x9"]])
est4=est3.fit()
est4.summary()