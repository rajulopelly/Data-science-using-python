# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:47:50 2019

@author: Unitech
"""
#preprocessing dataset
#1.How to load data file(s)?
#2.How to convert a variable to different data type?
#3.How to transpose a table?
#4.How to sort Data?
#5.How to create plots (Histogram, Scatter, Box Plot)?
#6.How to generate frequency tables?
#7.How to do sampling of Data set?
#8.How to remove duplicate values of a variable?
#9.How to group variables to calculate count, average, sum?
#10.How to recognize and treat missing values and outliers?
#11.How to merge / join data set effectively?

#Import Python Libraries
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv("C:/Users/Unitech/Downloads/loan.csv")

print(df)
#List first 5 records
print(df.head())
print(df.tail())

#Check types for all the columns
print(df.dtypes)
print(df.ndim)
print(df.size)
print(df.axes)
print(df.columns)

#Calculate mean value for each numeric column per each group
print(df["Credit Score"].mean())
#finding null values
print(df.isnull())

#df.isnull().sum()
#dropna()   Drop missing observations
#dropna(how='all')   Drop observations where all cells is NA
#dropna(axis=1, how='all')   Drop column if all the values aremissing
#dropna(thresh = 5)  Drop rows that contain less than 5 non-missing values
#fillna(0)  Replace missing values with zeros
#isnull()   returns True if the value is missing
#notnull()  Returns True for non-missing values

#Check types for all the columns
print(df.dtypes)

#Check whether there are null values in columns
print(df.isnull().sum())

print(df.isnull().sum().plot(kind= "pie"))

#you can draw histogram=hist,bargraph=bar,line plot=line,piechart=pie
#replacing null values
df["Credit Score"] = df["Credit Score"].fillna((df["Credit Score"].mean()))
print(df["Credit Score"])

df["Annual Income"] = df["Annual Income"].fillna((df["Annual Income"].mean()))
print(df["Annual Income"])

df["Months since last delinquent"] = df["Months since last delinquent"].fillna((df["Months since last delinquent"].mean()))
print(df["Months since last delinquent"])

df["Bankruptcies"] = df["Bankruptcies"].fillna((df["Bankruptcies"].mean()))
print(df["Bankruptcies"])
df["Tax Liens"] = df["Tax Liens"].fillna((df["Tax Liens"].mean()))
print(df["Tax Liens"])
df["Maximum Open Credit"] = df["Maximum Open Credit"].fillna((df["Maximum Open Credit"].mean()))
print(df["Maximum Open Credit"])

print(df.dropna(subset=["Years in current job"]))
print(df.dtypes)

print(df["Loan Status"].isnull().sum())
print(df["Loan Status"].value_counts())
print(df["Loan Status"].value_counts().plot(kind='bar'))

print(df["Loan Status"].value_counts())
print(df["Loan Status"].value_counts().plot(kind="bar"))
cleanloanstatus = {"Loan Status": {"Fully Paid": 1,"Charged Off": 2 }}
print(df.replace(cleanloanstatus, inplace= True))
print(df["Loan Status"].head())

print(df["Term"].value_counts())
print(df["Term"].value_counts().plot(kind='hist'))
cleanTerm = {"Term": {"Short Term": 1,"Long Term": 2 }}
print(df.replace(cleanTerm, inplace= True))
print(df["Term"].head())
print(df.dtypes)

print(df["Home Ownership"].value_counts())
print(df["Term"].value_counts().plot(kind='line'))

cleanownership = {"Home Ownership": {"Home Mortgage": 1,"Rent": 2,"Own Home": 3,"HaveMortgage": 4 }}
print(df.replace(cleanownership, inplace= True))
print(df["Home Ownership"].head())



print(df["Purpose"].value_counts())
print(df["Term"].value_counts().plot(kind='pie'))
cleanPurpose = {"Purpose": {"Debt Consolidation":1 ,"Business Loan":2 ,"small_business":3 ,
                "other":4 ,"Other":4 ,"renewable_energy":5 ,"Home Improvements":6,
                "Buy a Car":7 ,"vacation":8 ,"Educational Expenses":9 ,"Medical Bills":10 ,
                "moving":11 ,"wedding":12 ,"Take a Trip":13 ,"major_purchase":14 ,"Buy House":15 }}
print(df.replace(cleanPurpose, inplace= True))
print(df["Purpose"].head())

print(df["Years in current job"].value_counts())
print(df["Term"].value_counts().plot(kind='bar'))
cleanyearsofcurrentjob = {"Years in current job": { "10+ years": 10 ,"2 years":2 ,"3 years":3 ,"< 1 year": 1,
                          "4 years":4 ,"5 years":5 ,"6 years":6,"7 years":7 ,"8 years":8 ,"9 years":9 }}
print(df.replace(cleanyearsofcurrentjob, inplace= True))
print(df["Years in current job"].head())

print(df["Years of Credit History"].describe())
print(plt.boxplot(df["ears of Credit History"]))

print(df["Monthly Debt"].describe())
print(plt.boxplot(df["Monthly Debt"]))
print(plt.boxplot(df["Monthly Debt"]))
