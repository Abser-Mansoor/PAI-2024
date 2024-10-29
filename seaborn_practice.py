import numpy as np
import abc as ab
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')
sns.set_style('darkgrid')
plt.figure(figsize=(10,15))
plt.subplot(3,3,1)
sns.scatterplot(tips,x='total_bill',y='tip',hue='tip')
plt.subplot(3,3,2)
sns.boxplot(tips,x='total_bill',y='tip',hue='total_bill')
plt.subplot(3,3,3)
sns.boxenplot(tips,x='total_bill',y='tip',hue='tip')
plt.subplot(3,3,4)
sns.histplot(tips,x='total_bill',y='tip',color='red',bins=20)
plt.subplot(3,3,5)
sns.barplot(tips,x='day',y='total_bill',hue='day')
plt.subplot(3,3,6)
sns.lineplot(tips,x='total_bill',y='tip',color='green')
plt.subplot(3,3,7)
sns.pairplot(tips)
plt.subplot(3,3,8)
sns.heatmap(tips.select_dtypes(include='number').corr(),annot=True,cmap='coolwarm')
plt.subplot(3,3,9)
sns.jointplot(tips,x='total_bill',y='tip',kind='reg')
plt.show()
