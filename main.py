import numpy as np
import pandas as pd
from sklearn import preprocessing, model_selection, neighbors
import warnings
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
from collections import Counter

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace=True)
df.drop(['id'], axis=1, inplace=True) #Dropping the id column as it has no implication on whether a tumor is benign or malignant

X = np.array(df.drop(['class'], axis=1)) #All other columns except the class are the feattures
y = np.array(df['class']) #The class column is the label for this classification

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train) #Training the dataset

accuracy = clf.score(X_test, y_test) #Testing the accuracy of the classifier
print(accuracy)

input_data = []
print("Enter the tumor data of the patient\n")
for i in range(0, 9):
  ele = int(input())
  input_data.append(ele)
 
 element_measures = np.array([input_data])
 element_measures = input_measures.reshape(len(element_measures), -1)
 
 prediction = clf.predict(element_measures)
 print(prediction) #if array[2] is printed, then its malignant, and if array[4] is printed, then its beningn
 