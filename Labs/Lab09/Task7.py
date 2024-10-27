import numpy as np
import abc as ab
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# Separate dataset and age groups used to accomodate that dataset as the specified dataset was not provided

df = pd.read_csv("Global_sea_level_rise.csv")

df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

plt.figure(figsize=(12, 6))
plt.scatter(df['date'], df['mmfrom1993-2008average'], color='blue', alpha=0.6, label='Sea Level Rise (mm)')
plt.title('Global Sea Level Rise Over Time')
plt.xlabel('Year')
plt.ylabel('Sea Level (mm)')
plt.legend()
plt.show()
