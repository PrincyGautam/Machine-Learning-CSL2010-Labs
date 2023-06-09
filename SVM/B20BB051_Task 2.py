# -*- coding: utf-8 -*-
"""Lab6_Task_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11dZzdARKqv92sTZG0UGHibPfxYRA4j0z
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

df = pd.read_csv('/content/drive/MyDrive/IML_Dataset/Dataset_2.csv')

df.shape

df.head()

X = df.drop(['Experience', 'CCAvg', 'Mortgage'], axis=1)
Y = df['CreditCard']

df.isnull().any()

fig = plt.figure(figsize = (10,7))
ax = plt.axes(projection ="3d")
ax.scatter3D(X.iloc[:,0], X.iloc[:,1], X.iloc[:,2],marker='o', s=5, color='green')
plt.title("3D scatter plot")
plt.show()

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20)
print(X_train.shape, X_test.shape)

C={0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000}
svclass = LinearSVC(C=0.0001)
svclass = LinearSVC(C=0.001)
svclass = LinearSVC(C=0.01)
svclass = LinearSVC(C=0.1)
svclass = LinearSVC(C=1)
svclass = LinearSVC(C=10)
svclass = LinearSVC(C=100)
svclass = LinearSVC(C=1000)
svclass.fit(X_train, Y_train)

for num in C:
  Y_pred = svclass.predict(X_test)
  print('Score on test data with C=',num,'is',svclass.score(X_test, Y_test))

cnf_mat = confusion_matrix(Y_test, Y_pred)
clas_rep = classification_report(Y_test, Y_pred)
print('Confusion matrix \n',cnf_mat)
print('\n')
print('Classification report \n', clas_rep)

param_grid={'C':[0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000]}
grid = GridSearchCV(LinearSVC(), param_grid, cv=8)
grid.fit(X_train, Y_train)

print('Best value is |',grid.best_params_)