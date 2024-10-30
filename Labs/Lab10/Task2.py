#Overall Distribution
import numpy as np
import abc as ab
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ENB2012_data.csv')
plt.figure(figsize=(12,18))
plt.subplot(5,2,1)
sns.histplot(df['X1'],kde=True)
plt.subplot(5,2,2)
sns.histplot(df['X2'],kde=True)
plt.subplot(5,2,3)
sns.histplot(df['X3'],kde=True)
plt.subplot(5,2,4)
sns.histplot(df['X4'],kde=True)
plt.subplot(5,2,5)
sns.histplot(df['X5'],kde=True)
plt.subplot(5,2,6)
sns.histplot(df['X6'],kde=True)
plt.subplot(5,2,7)
sns.histplot(df['X7'],kde=True)
plt.subplot(5,2,8)
sns.histplot(df['X8'],kde=True)
plt.subplot(5,2,9)
sns.histplot(df['Y1'],kde=True)
plt.subplot(5,2,10)
sns.histplot(df['Y2'],kde=True)
plt.show()
