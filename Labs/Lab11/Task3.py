from sklearn.model_selection import train_test_split,KFold
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score,confusion_matrix
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv('derma.csv')
df = df.dropna()
X = df.values[:, :35]
y = df.values[:, 35]

print(X.shape, y.shape)

kf = KFold(10, shuffle=True, random_state=727)

for i, (train_index, test_index) in enumerate(kf.split(X)):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X[train_index], y[train_index])
    predictions = knn.predict(X[test_index])
    print(f'Iteration {i+1}:\nConfusion Matrix')
    print(confusion_matrix(y[test_index], predictions))
