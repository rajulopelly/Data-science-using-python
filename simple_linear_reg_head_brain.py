# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:04:51 2018
@author: Mahesh
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#reading the data
	
data=pd.read_csv('C:/Users/Unitech/Desktop/RAJU PYTHON/raju tvashtaa python/headbrain.csv')
print(data.head())
print(data.columns)

x=data.iloc[:,2:3].values
y=data.iloc[:,3:4].values
plt.scatter(x,y)
plt.show()

#splitting the data into training and test
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/4,random_state=0)

#fitting simple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

#predict the test result
y_pred=regressor.predict(x_test)

#To see the relationship between the training data values
plt.scatter(x_train,y_train,c='red')
plt.show()
print(len(y_pred))
#To see the relationship between the predicted brain weight values using scattered graph
plt.plot(x_test,y_pred)   
plt.scatter(x_test,y_test,c='red')
plt.xlabel('headsize')
plt.ylabel('brain weight')

#metrics
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
e=mean_squared_error(y_test,y_pred)
print(np.sqrt(e))
print("r2 score:")
print(r2_score(y_test,y_pred))
