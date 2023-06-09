# -*- coding: utf-8 -*-
"""B20BB051.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-egFi0OEMIjfMSOvoSvKwm2bpAlra_Ke
"""

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as pltlblblb
import numpy as np
import pandas as pd

df = pd.read_csv('/content/diabetes (1).csv')

df.describe()

df.head()

df_copy = df.copy()

from sklearn.preprocessing import StandardScaler
scaling=StandardScaler()
scaling.fit(df_copy)
Scaled_data=scaling.transform(df_copy)

from sklearn.model_selection import train_test_split
X = df_copy.drop('Outcome',axis=1)
Y = df_copy['Outcome']
x_train, x_test, y_train, y_test = train_test_split(X ,Y ,test_size=0.30 ,random_state=250)
print('Shape of x_train:', x_train.shape)
print('Shape of x_test:', x_test.shape)
print('Shape of y_train:', y_train.shape)
print('Shape of y_test:', y_test.shape)

from sklearn import metrics
lda = LinearDiscriminantAnalysis(n_components=1, solver='svd')
lda.fit(x_train,y_train)
predict_lda = lda.predict(x_test)
accuracy_lda = metrics.accuracy_score(y_test, predict_lda)
print('Accuracy from LDA: ', accuracy_lda)

principal=PCA(n_components=2)
principal.fit(Scaled_data)
x = principal.transform(Scaled_data)

print(x.shape) 

pltlb.figure()
pltlb.figure(figsize=(10,10))
pltlb.xticks(fontsize=12)
pltlb.yticks(fontsize=14)
pltlb.xlabel('Principal Component - 1',fontsize=20)
pltlb.ylabel('Principal Component - 2',fontsize=20)
pltlb.title("Principal Component Analysis",fontsize=20) 
pltlb.scatter(x[:,0],x[:,1], alpha=0.7, marker='o', s=40, cmap='cividis')

feat_cols = ['PC '+str(i) for i in range(x.shape[1])]
normalised = pd.DataFrame(x, columns=feat_cols)
normalised.head()

print('Explained variation per principal component: {}'.format(principal.explained_variance_ratio_))

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train, y_train)
predicted_knn=knn.predict(x_test)
accuracy_knn=metrics.accuracy_score(y_test, predicted_knn)
print('Accuracy from KNN:', accuracy_knn)

from sklearn.linear_model import LogisticRegression
logisticRegr= LogisticRegression()
logisticRegr.fit(x_train,y_train)
predict_lg = logisticRegr.predict(x_test)
accuracy_lg = metrics.accuracy_score(y_test,predict_lg)
print('Accuracy from logistic regression: ', accuracy_lg)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(random_state=250, hidden_layer_sizes=(80), activation='relu').fit(x_train, y_train) 
clf.n_layers_

pred_lab = clf.predict(x_test)

pred_lab

accuracy_mlp = metrics.accuracy_score(y_test, pred_lab)                            
print('Accuracy from MLP: ', accuracy_mlp*100)