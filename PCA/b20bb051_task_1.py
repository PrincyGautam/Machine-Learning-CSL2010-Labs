# -*- coding: utf-8 -*-
"""B20BB051_Task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w6Rixh7C_6o77TNVJsPPoKQXhRlZx5St
"""

import tensorflow as tf
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
# x_train and x_test parts contain greyscale RGB codes (from 0 to 255) 
# while y_train and y_test parts contain labels from 0 to 9 which represents which number they actually are.

print('x_train: ',x_train.shape)
print('x_test: ',x_test.shape)
print('y_train: ',y_train.shape)
print('y_test: ',y_test.shape)

import matplotlib.pyplot as plt

image_index = 9768 # You may select anything up to 60,000
print('The label is |',y_train[image_index]) # The label is 7
plt.imshow(x_train[image_index], cmap='Greys')

x_train.shape

x_train[image_index].shape

x_train = x_train.reshape(x_train.shape[0], 28, 28)        
x_test = x_test.reshape(x_test.shape[0], 28, 28)
input_shape = (28, 28)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255

print('x_train shape:', x_train.shape)
print('Number of images in x_train', x_train.shape[0])
print('Number of images in x_test', x_test.shape[0])
print(x_train[image_index].shape)

x_train.shape = 60000, 28, 28 
x_train_2d = x_train.reshape((60000,28*28))

from sklearn.preprocessing import StandardScaler
import numpy as np
standard_scalar = StandardScaler()
standardized_data = standard_scalar.fit_transform(x_train_2d)
print('The shape of standardized data is ',standardized_data.shape)

from sklearn.decomposition import PCA
pca = PCA(n_components=5)
principalComponents = pca.fit_transform(x_train_2d)

print('Explained variance: ',pca.explained_variance_ratio_)

print('Number of components required are: ',pca.n_components_)