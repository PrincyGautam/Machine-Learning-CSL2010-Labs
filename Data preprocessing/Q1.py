#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
cars = pd.read_csv(r"C:\Users\HP\Downloads\Cars93.csv")
cars


# In[ ]:


cars.isnull().sum()


# In[ ]:


cars.info()


# In[ ]:


#assigning a type 

         #Model = Nominal
         #Type = Ordinal
         #Max.Price = Ratio 
         #AirBags = Ordinal


# In[ ]:


cars.loc[:, cars.isnull().any()].columns


# In[ ]:


cars_fill_na=cars.fillna(0)


# In[ ]:


cars_fill_na


# In[ ]:


#dataframe after replacing NA values with 0
cars_fill_na.info()


# In[ ]:


#noise
M = cars['Model'].tolist()                            #created list of column to find the most common value
N = cars['Cylinders'].tolist()

def most_common(lst):                                 #function to find the most common value of the column
    return max(set(lst), key=lst.count)

def remove_noise1(x):                                 #here x is column name and this is a function to remove
    for i in range(len(cars[x])):                     #noise of string form
        if type(cars[x][i]) == type(str()):                
            cars[x][i] = most_common(N)
    return cars

def remove_noise2(y):                                 #here y is column name and this function is to remove 
    for i in range(len(cars[y])):                     #noise of integer form
        if cars[y][i].isnumeric():
            cars[y][i] = most_common(M)
    return cars
    
print(remove_noise1("Cylinders"))
print(remove_noise2("Model"))


# In[ ]:


#encoding categorical features
# Including columns which are of object datatype in modified dataframe
cars_mod = cars.select_dtypes(include=['object'])
# Viewing first few rows of data
cars_mod.head()


# In[ ]:


# Checking for any null values present in the dataset
cars_mod.isnull().sum()


# In[ ]:


# Encoding using get_dummies
cars_mod = pd.get_dummies(cars_mod, drop_first=True)


# In[ ]:


cars_mod


# In[ ]:


#normalise
# Including columns which are of integers datatype in modified dataframe
cars_1_mod = cars.select_dtypes(include=['float64','int64'])
# Viewing first few rows of data
cars_1_mod.head(93)


# In[ ]:


cars_1_mod.describe()


# In[ ]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = cars_1_mod.iloc[:,]
scaler.fit(X)
carsScaled=scaler.transform(X)


# In[ ]:


carsScaled


# In[ ]:


cars_fill_na.head()


# In[ ]:


X = cars_fill_na.iloc[:,0:]
Y = cars_fill_na.iloc[:,4]


# In[ ]:


#random split
from sklearn.model_selection import train_test_split
train_ratio = 0.70
validation_ratio = 0.20
test_ratio = 0.10

# train is now 70% of the entire data set
# the _junk suffix means that we drop that variable completely
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=1 - train_ratio)

# test is now 10% of the initial data set
# validation is now 20% of the initial data set
x_val, x_test, y_val, y_test = train_test_split(x_test, y_test, test_size=test_ratio/(test_ratio + validation_ratio)) 

print(x_train, x_val, x_test)

