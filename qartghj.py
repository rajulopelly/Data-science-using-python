# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 13:11:49 2019

@author: Unitech
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#reading the data	
df=pd.read_csv("C:/Users/Unitech/Downloads/headbrain.csv")
print(df.columns)
x=df.iloc[:,2:3].values
y=df.iloc[:,3:4].values
plt.scatter(x,y)
plt.show()
"""
import statsmodels.api as sm # import statsmodels 

X = df["RM"] ## X usually means our input variables (or independent variables)
y = target["MEDV"] ## Y usually means our output/dependent variable
X = sm.add_constant(X) ## let's add an intercept (beta_0) to our model

# Note the difference in argument order
model = sm.OLS(y, X).fit() ## sm.OLS(output, input)
predictions = model.predict(X)

# Print out the statistics
model.summary()
"""
#splitting the data into training and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/4,random_state=123)

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
e=mean_squared_error(y_test,y_pred)
print(np.sqrt(e))
print("r2 score:")
print(r2_score(y_test,y_pred))

