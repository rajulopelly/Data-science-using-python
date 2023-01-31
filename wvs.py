# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:45:23 2019

@author: Unitech
"""

#Import Python Libraries
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl
df= pd.read_csv("C:/Users/Unitech/Desktop/RAJU PYTHON/WVS.csv")

print(df)
df = df[['name','gender','age','religion','country','degree','poverty']]
print(df.head())
print(df.dtypes)
print(df.info())
print(df.interpolate())
print(df.isnull().sum())
#data cleaning
print(df["gender"].describe())
print(df["gender"].value_counts())
df.gender[df.gender == 'male'] = 1
df.gender[df.gender == 'female'] = 2
print(df.head())
print(df["gender"].value_counts().plot(kind="bar"))

print(df["age"].describe())
print(df["age"].head())
# Make boxplot for age data
x=sns.boxplot(df["age"])
print(x)

print(df["religion"].value_counts())
df.religion[df.religion == "no"] = 1
df.religion[df.religion == "yes"] = 2
print(df.head())
print(df["religion"].describe())
print(df["religion"].value_counts().plot(kind="hist"))

print(df["country"].value_counts())
df.country[df.country == "Australia"] = 1
df.country[df.country == "USA"] = 2
df.country[df.country == "Norway"] = 3
df.country[df.country == "Sweden"] = 4
df.country[df.country == "India"] = 5
print(df["country"].head())
print(df["country"].tail())
print(df["country"].value_counts().plot(kind="pie"))

print(df["degree"].head())
print(df["degree"].describe())
df.degree[df.degree == 'no'] = 1
df.degree[df.degree == 'yes'] = 2
print(df["degree"].head())

print(df["poverty"].value_counts())
print(df["poverty"].describe())
df.poverty[df.poverty == 'Too Little'] = 1
df.poverty[df.poverty == 'About Right'] = 2
df.poverty[df.poverty == 'Too Much'] = 3
print(df["poverty"].head())

print(df.dtypes)
print(df.head())
#convert data categorical into numerical
df['gender'] = df['gender'].astype('float64')
print(df['gender'])
df['religion'] = df['religion'].astype('float64')
print(df['religion'])
df['country'] = df['country'].astype('float64')
print(df['country'])
df['degree'] = df['degree'].astype('float64')
print(df['degree'])
df['poverty'] = df['poverty'].astype('float64')
print(df['poverty'])

#insights

