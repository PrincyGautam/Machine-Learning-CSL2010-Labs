# -*- coding: utf-8 -*-
"""Task 1  .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eed-0mdtF2GqMyiEwQ_i1asoPGJWprGI
"""

from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report 
import graphviz
from sklearn import tree

df = pd.read_csv("/content/drugs.csv")
df.head()

#feature = Age, Sex, BP, Cholestrol, Na_to_K
#target =  Drug

df.isnull().any()
#no null values

#'Age': numerical 
#'Sex': Nominal 
#'BP' : ordinal 
#'Cholesterol' :ordinal 
#'Na_to_K' : numerical
#'Drug' : categorical

data = pd.read_csv("/content/drugs.csv")
lb = LabelEncoder()

data['Sex_n']=lb.fit_transform(data['Sex'])
data['Bp_n']=lb.fit_transform(data['BP'])
data['Cholesterol_n']=lb.fit_transform(data['Cholesterol'])
data['drug_n']=lb.fit_transform(data['Drug'])

data_new = data.drop(['Sex','BP','Cholesterol','Drug'],axis = 'columns')
print(data_new)

#------------------------------------------------------------------------LAB 5 PART 2---------------------------------------------------------------------------------------------

X =  df.iloc[:,:-1].values
le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F','M'])
X[:,1] = le_sex.transform(X[:,1]) 


le_BP = preprocessing.LabelEncoder()
le_BP.fit([ 'LOW', 'NORMAL', 'HIGH'])
X[:,2] = le_BP.transform(X[:,2])


le_Chol = preprocessing.LabelEncoder()
le_Chol.fit([ 'NORMAL', 'HIGH'])
X[:,3] = le_Chol.transform(X[:,3]) 

X[0:5]

Y =  df.iloc[:,-1:].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, shuffle = True, random_state=55)
print(X_train.shape,X_test.shape)

model1 = DecisionTreeClassifier(criterion='entropy', random_state=55)
model1.fit(X_train, Y_train)

Y_pred1= model1.predict(X_test)
print("Accuracy |",metrics.accuracy_score(Y_test, Y_pred1))

cnf_mat1= confusion_matrix(Y_test, Y_pred1) 
print('Confusion matix |\n', cnf_mat1)

print(classification_report(Y_test, Y_pred1))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, shuffle = True, random_state=55)
print(X_train.shape,X_test.shape)

model2 = DecisionTreeClassifier(criterion='gini',random_state=55)
model2.fit(X_train, Y_train)

Y_pred2 = model2.predict(X_test)
print('Model Accuracy | ',metrics.accuracy_score(Y_test, Y_pred2))

cnf_mat2= confusion_matrix(Y_test, Y_pred2) 
print('Confusion matix |\n', cnf_mat2)

print(classification_report(Y_test, Y_pred2))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, shuffle = True, random_state=55)
print(X_train.shape,X_test.shape)

model3 = DecisionTreeClassifier(criterion='gini',random_state=55)
model3.fit(X_train, Y_train)

Y_pred3 = model3.predict(X_test)
print('Model Accuracy | ',metrics.accuracy_score(Y_test, Y_pred3))

cnf_mat3= confusion_matrix(Y_test, Y_pred3) 
print('Confusion matix |\n', cnf_mat3)

print(classification_report(Y_test, Y_pred3))

featureNames = df.columns[0:5] 
targetNames = df["Drug"].unique().tolist()
drug_tree1 = tree.export_graphviz(model1, feature_names=featureNames, class_names= np.unique(Y_train), filled=True, rounded=True)
graph1 = graphviz.Source(drug_tree1, format="png") 
print('MODEL 1 | \n')
graph1

drug_tree2 = tree.export_graphviz(model2, feature_names=featureNames, class_names= np.unique(Y_train), filled=True, rounded=True)
graph2 = graphviz.Source(drug_tree2, format="png") 
print('MODEL 2 | \n')
graph2

drug_tree3 = tree.export_graphviz(model3, feature_names=featureNames, class_names= np.unique(Y_train), filled=True, rounded=True)
graph3 = graphviz.Source(drug_tree3, format="png")
print('MODEL 3 | \n') 
graph3