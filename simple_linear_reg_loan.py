# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 12:56:47 2018

@author: Mahesh
"""

#Simple Linear Regression Model using scikit-learn.

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#plt.rcParams['figure.figsize'] = (20.0, 10.0)

# Reading Data
data = pd.read_csv('loan.csv')
print(data.shape)
print(data.head())
data.fillna(data.mean())
print(data.isnull().sum())
"""
a linear relationship between current credit balance and credit score. 
.
"""
data_columns=data.columns.values
print("columns")
print(data.columns)
x_credit_balance=data["Current Credit Balance"].values
print("credit balance data")
print(x_credit_balance)
y_loan_credit_score=data["Credit Score"].values
print("Credit Score data")
print(y_loan_credit_score)

"""
# Cannot use Rank 1 matrix in scikit learn
x_credit_balance= x_credit_balance.reshape((m, 1))
# Creating Model
reg = LinearRegression()
# Fitting training data
reg = reg.fit(x_credit_balance, y_loan_credit_score)
# Y Prediction
Y_pred = reg.predict(x_credit_balance)

# Calculating RMSE and R2 Score
mse = mean_squared_error(y_loan_credit_score, Y_pred)
rmse = np.sqrt(mse)
r2_score = reg.score(x_credit_balance,y_loan_credit_score)
print("Root Mean squared Error")
print(np.sqrt(mse))
print(r2_score)
"""