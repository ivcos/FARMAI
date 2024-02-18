import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import pickle
import requests
import json


# Calculate Mean Absolute Error to determine how well the model selected performs on new unseen data
def mae(y_test, y_pred):
    sum_test = 0.0
    for i in range(len(y_test)):
        sum_test += abs(y_test[i] - y_pred[i])
    return sum_test / len(y_test)

# Load the dataset into dependent and independent variables
dataset = pd.read_csv('app/data/sensors.csv')
X = dataset.iloc[:, 1].values
y = dataset.iloc[:, 2].values

# Split the dataset into the training set and test set.
# The model is trained on the Test set and model is then tested agaisnt the hold out test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)


# Instantiate and  Train the model
regressor=LinearRegression()
regressor.fit(X_train.reshape(-1, 1), y_train)
# Make the prediction
y_pred = regressor.predict(X_test.reshape(-1, 1))
print("y_pred", y_pred)
print("y_test", y_test)
# check parameters
print(regressor.intercept_)
print(int(regressor.coef_))
# Check Accuracy
print("Mean Absolute Error: ", mae(y_test, y_pred))
# Save the Linear Regressor model to a file for later use
pickle.dump(regressor, open('app/data/sensor-regessor-model.pk1' , 'wb'))

# Loading model to compare the results
regressor_model = pickle.load(open('app/data/sensor-regessor-model.pk1','rb'))
print(regressor.predict([[28]]))