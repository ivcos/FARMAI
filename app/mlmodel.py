import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json

# Load the dataset
dataset = pd.read_csv('app/data/sensor.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values
print(X)
print(y)
# Split the dataset into the training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

print(X_train)
print(len(X_train))
print(X_test)
print(len(X_test))

regressor=LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
print("y_pred", y_pred)
print(regressor.intercept_)
print(int(regressor.coef_))