import pandas as pd

df = pd.read_excel('employee.xlsx')
df = df[(df['Year'] == 2022)]
print(df)
