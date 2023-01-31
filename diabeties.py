# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 19:28:07 2019

@author: Unitech
"""
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_boston
df= pd.read_csv("C:/Users/Unitech/Downloads/Boston.csv")
x=df.iloc[:,0:14].values
y=df.iloc[:,14:15].values
plt.scatter(x,y)
plt.show()
#splitting the data into training and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/4,random_state=123)

#fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
#makeing a linear regression model
regressor.fit(x_train,y_train)
#names of daraset
names =[i for i in list (x)]
print(names)
regressor.intercept_
#the coefficients
regressor.coef_
#predicting the data
print("mean square error %.2f:" %np.mean((regressor.predict(x_test)-y_test)**2))
print("variance score %.2f:" % regressor.score(x_test,y_test))
pd.DataFrame(zip(names,regressor.coef_[0].tolist()),columns=["names","coefficients"])
plt.scatter(regressor.predict(x_test),y_test)
plt.show()
###############################OR##################################
###########################STATSMODELS#############################
import statsmodels.api as sm
from statsmodels.sandbox.regression.predstd import wls_prediction_std
model1=sm.OLS(y_train,x_train)
x=model1.fit()
x.summary()
#we can drop the p values of variable which is "p>0.05" 
model1=sm.OLS(y_train,x_train[["x2","x3","x7","x9","x10","x12","x13","x14"]])
x2=model1.fit
x2.summary()