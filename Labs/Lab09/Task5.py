import numpy as np
import abc as ab
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# Separate dataset and age groups used to accomodate that dataset as the specified dataset was not provided

df = pd.read_csv("heart.csv")

gender_counts = df['sex'].value_counts()

gender_labels = ['Male','Female']

plt.figure(figsize=(8, 6))
plt.pie(gender_counts, labels=gender_labels, autopct='%1.1f%%')
plt.title('Distribution of Patient Genders')
plt.axis('equal')
plt.show()
