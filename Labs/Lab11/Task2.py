from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("heart.csv")
df.dropna(inplace=True)
x = df.drop('target',axis=1)
y = df['target']

accs = []
for random_seed in range(1, 11):
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=random_seed)

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X_train, Y_train)
    predictions = knn.predict(X_test)

    accs.append(accuracy_score(Y_test, predictions))

npaccs = np.array(accs)
npaccs.sort()
print(accs)
print("MAX ACCURACY: ", npaccs[-1])
print("MIN ACCURACY: ", npaccs[0])
