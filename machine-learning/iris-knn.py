#!/usr/bin/env python

# Importing the Required Libraries and Loading the Dataset
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline
dataset = pd.read_csv("data/iris-knn.csv")
# Dividing Data Into Features and Labels
feature_columns = ['SepalLengthCm', 'SepalWidthCm',
                   'PetalLengthCm', 'PetalWidthCm']
X = dataset[feature_columns].values
y = dataset['Species'].values
# Visualizing Dataset using Pairplot
plt.figure()
sns.pairplot(dataset.drop("Id", axis=1), hue="Species",
             size=3, markers=["o", "s", "D"])
plt.show()
# Visualizing Dataset using Boxplot
plt.figure()
dataset.drop("Id", axis=1).boxplot(by="Species", figsize=(15, 10))
plt.show()
# Splitting the Data into Training and Testing Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

# Fitting the Model and Making Predictions
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
# Confusion Matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print('confusion matrix', confusion_matrix)
# Calculating Model Accuracy
accuracy = accuracy_score(y_test, y_pred)*100
print('Accuracy of the model:' + str(round(accuracy, 2)) + ' %.')
# Performing 10 fold Cross Validation
k_list = list(range(1, 50, 2))
cv_scores = []
for k in k_list:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())
# Finding Best K
best_k = k_list[cv_scores.index(max(cv_scores))]
print("The optimal number of neighbors is %d." % best_k)
print(cv_scores)
