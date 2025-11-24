#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 14:33:23 2025

@author: rbarcrosspbar
"""

# Import numpy
import numpy as np

# Import matplotlib as an alias plt and set the style
import matplotlib.pyplot as plt

# plt.style.use('seaborn-darkgrid')

# Import linear_model and dataset from sklearn
from sklearn import linear_model, datasets

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

#%%
# Use only one feature as a independent variable
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the independent data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
# diabetes_X_test[:2]
#%%
# Dependent variable 
diabetes_y = diabetes.target

# Split the dependent data into training/testing sets
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
diabetes_y_test 
#%%
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)
#%%
# Mean squared error
print('Mean squared error: %.2f' %
      np.mean((regr.predict(diabetes_X_test)-diabetes_y_test)**2))
#%%
# Calculate variance score
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))

# Plot outputs
plt.figure(figsize=(10, 7))
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, regr.predict(
    diabetes_X_test), color='blue', linewidth=3)
plt.title('Linear Regression Model', fontsize=14)
plt.xlabel('Independent Variable', fontsize=12)
plt.ylabel('Dependent Variable', fontsize=12)
plt.show()