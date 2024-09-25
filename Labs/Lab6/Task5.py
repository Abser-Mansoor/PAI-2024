import pandas as pd

df = pd.read_csv('alcohol-consumption-vs-gdp-per-capita.csv')
print(df.loc[30:49])
