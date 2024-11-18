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

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=7)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

accuracies = []
precisions = []
k = range(1,251)

for i in k :
    neighbour = KNeighborsClassifier(n_neighbors=i)
    neighbour.fit(x_train,y_train)
    y_pred = neighbour.predict(x_test)
    accuracies.append(accuracy_score(y_test,y_pred))
    precisions.append(precision_score(y_test,y_pred,average='binary'))

print(f"Best K: {accuracies.index(max(accuracies))} with accuracy: {max(accuracies)} and precision: {precisions[accuracies.index(max(accuracies))]}")
print(f"Worst K: {accuracies.index(min(accuracies))} with accuracy: {min(accuracies)} and precision: {precisions[accuracies.index(min(accuracies))]}")

x = np.arange(2)
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))
bar_acc = ax.bar(x - width/2, [accuracies.index(max(accuracies)),accuracies.index(min(accuracies))], width, label='Accuracy', color='b')
bar_prec = ax.bar(x + width/2, [precisions[accuracies.index(max(accuracies))], precisions[accuracies.index(min(accuracies))]], width, label='Precision', color='g')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Accuracy and Precision for Best and Worst k Values')
ax.set_xticks(x)
ax.set_xticklabels(['Best K','Worst K'])
ax.legend()

# Display the plot
plt.show()
