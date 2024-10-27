import numpy as np
import abc as ab
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# Separate dataset and age groups used to accomodate that dataset as the specified dataset was not provided

df = pd.read_csv("heart.csv")

age_bins = [30,40, 50, 60, 70, 100]
age_labels = ['30-40', '41-50', '51-60', '61-70', '71 and above']

df['Age Groups'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

age_counts = df['Age Groups'].value_counts()

age_counts = age_counts.dropna()

plt.figure(figsize=(8, 6))
plt.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Patient Ages')
plt.axis('equal')
plt.show()
