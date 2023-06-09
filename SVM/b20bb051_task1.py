# -*- coding: utf-8 -*-
"""B20BB051_Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZdCKXQY2J2Ya6zv3xEe27xscMxgwoEZa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, classification_report

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

data = pd.read_csv('/content/drive/MyDrive/IML_Dataset/Dataset.csv')

#checking the shape
data.shape

#checking the head 
data.head()

#separating the features and target of the data
X = data.iloc[:,:-1]
Y = data.iloc[:,-1]

#splitting the data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=20)
print(X_train.shape, X_test.shape)

#train the model
svclassifier = LinearSVC(C=1)
svclassifier.fit(X_train, Y_train)

#prediction on test data and printing score
Y_pred = svclassifier.predict(X_test)
score = svclassifier.score(X_test, Y_test)
print('Score on test data |',score)

cnf_mat = confusion_matrix(Y_test, Y_pred)
clas_rep = classification_report(Y_test, Y_pred)
print('Confusion matrix |\n',cnf_mat)
print('Classification report |\n', clas_rep)