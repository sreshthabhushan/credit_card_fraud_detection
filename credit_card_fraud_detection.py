# -*- coding: utf-8 -*-
"""credit_card_fraud_detection

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11HoTcyAn-rVOFSSqjOhcCr8riRRRkRR7

Importing the Dependencies
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# loading the dataset to a Pandas Data-Frame
credit_card_data = pd.read_csv('/content/credit_card.csv')

# first 5 rows of the dataset
credit_card_data.head()

# last 5 rows of the dataset
credit_card_data.tail()

# dataset information
credit_card_data.info()

# checking the number of missing values in each column
credit_card_data.isnull().sum()

credit_card_data.shape

credit_card_data.isnull().sum()

# analyze the distribution of data of Amount
fig, ax = plt.subplots(figsize=(8, 8))
sns.distplot(credit_card_data.Amount)

"""Replace the missing values with Median value"""

credit_card_data['Amount'].fillna(credit_card_data['Amount'].median(), inplace=True)

credit_card_data.isnull().sum()

# analyze the distribution of data of Class
fig, ax = plt.subplots(figsize=(8, 8))
sns.distplot(credit_card_data.Class)

credit_card_data['Class'].fillna(credit_card_data['Class'].median(), inplace=True)

credit_card_data.isnull().sum()

credit_card_data['V13'].fillna(credit_card_data['V13'].median(), inplace=True)
credit_card_data['V14'].fillna(credit_card_data['V14'].median(), inplace=True)
credit_card_data['V15'].fillna(credit_card_data['V15'].median(), inplace=True)
credit_card_data['V16'].fillna(credit_card_data['V16'].median(), inplace=True)
credit_card_data['V17'].fillna(credit_card_data['V17'].median(), inplace=True)
credit_card_data['V18'].fillna(credit_card_data['V18'].median(), inplace=True)
credit_card_data['V19'].fillna(credit_card_data['V19'].median(), inplace=True)
credit_card_data['V20'].fillna(credit_card_data['V20'].median(), inplace=True)
credit_card_data['V21'].fillna(credit_card_data['V21'].median(), inplace=True)
credit_card_data['V22'].fillna(credit_card_data['V22'].median(), inplace=True)
credit_card_data['V23'].fillna(credit_card_data['V23'].median(), inplace=True)
credit_card_data['V24'].fillna(credit_card_data['V24'].median(), inplace=True)
credit_card_data['V25'].fillna(credit_card_data['V25'].median(), inplace=True)
credit_card_data['V26'].fillna(credit_card_data['V26'].median(), inplace=True)
credit_card_data['V27'].fillna(credit_card_data['V27'].median(), inplace=True)
credit_card_data['V28'].fillna(credit_card_data['V28'].median(), inplace=True)

credit_card_data.isnull().sum()

# distribution of legit transactions & fraudulent transactions
credit_card_data['Class'].value_counts()

"""This Dataset is highly unbalanced

0 ---> Normal Transaction,
1 ---> Fraudulent Transaction
"""

# separating the data for analysis
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

print(legit.shape)
print(fraud.shape)

# statistical measures of the data
legit.Amount.describe()

fraud.Amount.describe()

# compare the values for both transactions
credit_card_data.groupby('Class').mean()

"""Under-Sampling

Build a sample dataset containing similar distribution of normal transactions and fraudulent transactions

Number of Fraudulent Transaction ---> 104
"""

legit_sample = legit.sample(n=104)

"""Concatenate two Data-Frames"""

new_dataset = pd.concat([legit_sample, fraud], axis=0)

new_dataset.head()

new_dataset.tail()

new_dataset['Class'].value_counts()

new_dataset.groupby('Class').mean()

"""Splitting the data into Features & Targets"""

X = new_dataset.drop(columns='Class', axis=1)
Y = new_dataset['Class']

print(X)

print(Y)

"""Split the data into Training data & Testing Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""Model Training

Logistic Regression
"""

model = LogisticRegression()

# training the Logistic Regression Model with Traing Data
model.fit(X_train, Y_train)

"""Model Evaluation

Accuracy Score
"""

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training data : ', training_data_accuracy)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score on Test Data : ', test_data_accuracy)