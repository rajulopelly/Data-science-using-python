# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 16:03:33 2019

@author: Unitech
"""
import numpy as np
import pandas as pd
import scipy as sp
import matplotlib.pyplot as plt
import sklearn as skl
import seaborn as sns
df=pd.read_csv("C:/Users/Unitech/Desktop/Insurance Data.csv")
print(df)
df.info
print(df.shape)
print(df.index)
print(df.values)
print(df.dtypes)
print(df.isnull().sum())
print(df.size)
# rename one or more columns
print(df.rename(columns={"Age":"age", "Gender":"gender", "Job Title":"JobTitle"}, inplace=True))
#if you want to drop a variable in python
#df.drop([‘column_x’, ‘column_y’], axis=1, inplace=True)
print(df.describe())
print(df["age"].mean())
df["age"] = df["age"].fillna((df["age"].mean()))
print(df["age"])
df["age"]=df["age"].astype("int64")
print(df["age"])
print(df["age"].value_counts().plot(kind = "box"))
print(df["age"].describe())
print(df["gender"])
cleanGender = {"gender": {"M": 1,"F": 2 }}
print(df.replace(cleanGender, inplace= True))
print(df["gender"].head())
print(df["gender"].isnull().sum())
#df["Gender"] = df["Gender"].fillna((df["Gender"].mode()))
df["gender"] = df["gender"].replace(np.nan,1.0)
print(df["gender"])
print(df["gender"].value_counts().plot(kind = "bar"))
df["gender"] = df["gender"].astype("int64")
#violin plot
#sns.violinplot(df['age'], df['gender']) 
#sns.despine()

print(df["Marital Status"].value_counts())
cleanMaritalStatus = {"Marital Status": {"Married": 1,"Divorced": 2,"Single": 3 }}
print(df.replace(cleanMaritalStatus, inplace= True))
print(df["Marital Status"].isnull().sum())
print(df["Marital Status"].value_counts())
df["Marital Status"] = df["Marital Status"].replace(np.nan,1.0)
print(df["Marital Status"])
print(df["Marital Status"].value_counts().plot(kind = "pie"))
df["Marital Status"] = df["Marital Status"].astype("int64")

print(df["Family Members"].value_counts())
print(df["Family Members"].isnull().sum())
df["Family Members"] = df["Family Members"].fillna(df["Family Members"].mean())
print(df["Family Members"].head())
print(df["Family Members"].describe())
df["Family Members"] = df["Family Members"].astype('int64')
print(df["Family Members"])
print(df["Family Members"].value_counts().plot(kind = "bar"))

print(df["Education"].value_counts())
print(df["Education"].isnull().sum())
df.Education[df.Education == "BD"] = 1
df.Education[df.Education == "MD"] = 2
df.Education[df.Education == "PD"] = 3
df.Education[df.Education == "LHS"] = 4
df.Education[df.Education == "UHS"] = 5
df.Education[df.Education == "NE"] = 6
print(df["Education"].mode())
df["Education"] = df["Education"].replace(np.nan,1.0)
print(df["Education"])
print(df["Education"].value_counts().plot(kind = "pie"))
df["Education"] = df["Education"].astype("int64")
print(df["Occupation"].value_counts())
print(df["Occupation"].isnull().sum())
df.Occupation[df.Occupation == "SPT"] = 1
df.Occupation[df.Occupation == "SE"] = 2
df.Occupation[df.Occupation == "SFT"] = 3
print(df["Occupation"].mode())
df["Occupation"] = df["Occupation"].replace(np.nan,1.0)
print(df["Occupation"])
df["Occupation"] = df["Occupation"].astype("int64")
print(df["Occupation"].value_counts().plot(kind = "hist"))

print(df["JobTitle"].value_counts())
print(df["JobTitle"].isnull().sum())
df.JobTitle[df.JobTitle == "FH"] = 1
df.JobTitle[df.JobTitle == "PG"] = 2
df.JobTitle[df.JobTitle == "DD"] = 3
df.JobTitle[df.JobTitle == "BA"] = 4
df.JobTitle[df.JobTitle == "RR"] = 5
df.JobTitle[df.JobTitle == "PR"] = 6
df.JobTitle[df.JobTitle == "OT"] = 7
df.JobTitle[df.JobTitle == "OM"] = 8
df.JobTitle[df.JobTitle == "CB"] = 9
df.JobTitle[df.JobTitle == "CF"] = 10
df.JobTitle[df.JobTitle == "OC"] = 11
df.JobTitle[df.JobTitle == "PA"] = 12
print(df["JobTitle"].value_counts())
print(df["JobTitle"].head())
df["JobTitle"] = df["JobTitle"].replace(np.nan,1.0)
df["JobTitle"] = df["JobTitle"].astype("int64")
print(df["JobTitle"].value_counts().plot(kind = "pie"))

print(df["Income"].isnull().sum())
df["Income"] = df["Income"].fillna(df["Income"].mean())
print(df["Income"].value_counts().plot(kind = "box"))
#q1 = df["Income"].quantile(0.25)
#print(q1)
#q3 = df["Income"].quantile(0.75)
#print(q3)
#Interquartile range
#iqr = q3-q1 
#print(iqr)
#lower_bound = q1-1.5*iqr
#print(lower_bound)
#upper_bound = q3+1.5*iqr
#print(upper_bound)
#df["Income"] = df.loc[(df["Income"] > lower_bound) & (df["Income"] < upper_bound)]
#print(df["Income"])
print(df["Income"].describe())
print(df["Income"].value_counts().plot(kind = "box"))
df["Income"] = df["Income"].astype('int64')
#the income of each person is in lachs so...
df["Income"] = df["Income"]*100000
print(df["Income"].head())

print(df["Current Coverage(In Rs)"].isnull().sum())
df["Current Coverage(In Rs)"] = df["Current Coverage(In Rs)"].fillna(df["Current Coverage(In Rs)"].mean())
print(df["Current Coverage(In Rs)"].describe())
print(df["Current Coverage(In Rs)"].value_counts().plot(kind = "box"))
#qu1 = df["Current Coverage(In Rs)"].quantile(0.25)
#print(qu1)
#qu3 = df["Current Coverage(In Rs)"].quantile(0.75)
#print(qu3)
#Interquartile range
#3iqrt = qu3-qu1 
#print(iqrt)
#lowerbound = qu1-1.5*iqrt
#print(lowerbound)
#upperbound = qu3+1.5*iqrt
#print(upperbound)
#df["Current Coverage(In Rs)"] = df.loc[(df["Current Coverage(In Rs)"] > lowerbound) & (df["Income"] < upperbound)]
df["Current Coverage(In Rs)"] = df["Current Coverage(In Rs)"].astype('int64')
print(df["Current Coverage(In Rs)"])
print(df["Current Coverage(In Rs)"].head())

print(df["New Coverage(In Rs)"].isnull().sum())
df["New Coverage(In Rs)"] = df["New Coverage(In Rs)"].fillna(df["New Coverage(In Rs)"].mean())
print(df["New Coverage(In Rs)"].describe())
df["New Coverage(In Rs)"] = df["New Coverage(In Rs)"].astype('int64')
print(df["New Coverage(In Rs)"])
print(df["New Coverage(In Rs)"].value_counts().plot(kind = "box"))

print(df["Current Product"].value_counts())
cleanCurrentProduct = {"Current Product": {"No": 1,"Yes": 2 }}
print(df.replace(cleanCurrentProduct, inplace= True))

print(df["Current Product"].head())
df["Current Product"] = df["Current Product"].replace(np.nan,1.0)

df["Current Product"] = df["Current Product"].astype("int64")
print(df["Current Product Type"].value_counts())

cleanCurrentProductType = {"Current Product Type": {"ANS": 1,"TLE": 2,"INV": 3,"PMT": 4,"END": 5 }}
print(df.replace(cleanCurrentProductType, inplace= True))
df["Current Product Type"] = df["Current Product Type"].replace(np.nan,1.0)
print(df["Current Product Type"].head( ))
df["Current Product Type"] = df["Current Product Type"].astype("int64")

print(df["New Product Type"].value_counts())
cleanCurrentProductType = {"New Product Type": {"ANS": 1,"TLE": 2,"INV": 3,"PMT": 4,"END": 5 }}
print(df.replace(cleanCurrentProductType, inplace= True))
df["New Product Type"] = df["New Product Type"].replace(np.nan,1.0)
print(df["New Product Type"].head( ))
df["New Product Type"] = df["New Product Type"].astype("int64")

print(df["Rating"].value_counts())
cleanRating = {"Rating": {"Cold": 1,"Warm": 2,"Hot": 3 }}
print(df.replace(cleanRating, inplace= True))
df["Rating"] = df["Rating"].replace(np.nan,1.0)
print(df["Rating"].head( ))
df["Rating"] = df["Rating"].astype("int64")
#Customer rating status distribution
sns.countplot(df["Rating"], data=df)
plt.show()
print(df["Converted"].value_counts())
df.Converted[df.Converted == "NotConverted"] = 0
df.Converted[df.Converted == "Converted"] = 1
df["Converted"] = df["Converted"].replace(np.nan,1.0)
print(df["Converted"].head())
df["Converted"] = df["Converted"].astype("int64")

print(df["Status"].value_counts())
df.Status[df.Status == "Converted"] = 1
df.Status[df.Status == "QG"] = 2
df.Status[df.Status == "PS"] = 3
df.Status[df.Status == "PN"] = 4
df.Status[df.Status == "PW"] = 5
df.Status[df.Status == "DR"] = 6
df.Status[df.Status == "NW"] = 7
df.Status[df.Status == "ARS"] = 8
df.Status[df.Status == "PR"] = 9
df.Status[df.Status == "PP"] = 10
df.Status[df.Status == "AS"] = 11
df["Status"] = df["Status"].replace(np.nan,1.0)
print(df["Status"].head())
df["Status"] = df["Status"].astype("int64")
print(df["Status"])
print(df["Status"].value_counts().plot(kind = "pie"))

print(df[["Current Coverage(In Rs)","Current Product Type"]].corr())
print(df['Current Coverage(In Rs)'].corr(df['Current Product Type'], method= 'spearman'))
print(df['age'].corr(df['Marital Status'], method= 'spearman'))
print(df.drop("Status", axis=1, inplace=True))
#system can unable to do modelling on float or categorical data we have to convert 
#entire into numerical
#
# Split the data into training/testing sets
x=df.iloc[:,:-1].values
print(x)
y=df.iloc[:,-1].values
#Barplot for the dependent variable
sns.countplot(y,data=df, palette='hls')
plt.show()

#data partitioning
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=123)
# import the class
from sklearn.linear_model import LogisticRegression
# instantiate the model (using the default parameters)
logreg = LogisticRegression()
# fit the model with data
logreg.fit(x_train,y_train)
print(logreg.coef_)
print(logreg.intercept_)
print(logreg.score)
#we can predicting on testing data
y_pred=logreg.predict(x_test)
# import the metrics class then find confusion matrix
from sklearn import metrics
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)
# name  of classes
class_names=[0,1] 
fig, ax = plt.subplots()
# create heatmap
sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap="YlGnBu" ,fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title('Confusion matrix')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#Precision is about being precise, i.e., how accurate your model is. 
#In other words, you can say, when a model makes a prediction, how often it is correct.
print("Precision:",metrics.precision_score(y_test, y_pred))
#If there are persons who converted in the test set and your Logistic Regression model can identify it 58% of the time.
print("Recall:",metrics.recall_score(y_test, y_pred))
#Receiver Operating Characteristic(ROC) curve is a plot of the true positive rate against the 
#false positive rate. It shows the tradeoff between sensitivity and specificity
y_pred_proba = logreg.predict_proba(x_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()
"""                      OR
u can impliment the algorithm using statistic model
"""

x = df.drop('Converted',1)
y = df['Converted']
import statsmodels.api as sm
logit_model=sm.Logit(y,x)
result=logit_model.fit()
print(result.summary())
#thep value should be below the "0.05". only one variable "x10" has more than that.
#so we can remove that insignificant variable
df1 = df.drop('Current Product Type',1)
X = df1.drop('Converted',1)
logit_model1=sm.Logit(y,X)
result1=logit_model1.fit()
print(result1.summary())
