import pandas as pd

df1 = pd.read_csv('Products.csv')
df2 = pd.read_csv('Orders.csv')
print(df1.head(5))
print(df1.tail(10))
print("\nDataFrame two:\n")
print(df2.head(5))
print(df2.tail(10))
Merged = pd.merge(df1,df2,on='ProductID')
Merged['Revenue'] = Merged['Quantity'] * Merged['Price']
print(Merged)
print(f"\n\nTotal Revenue is: {Merged['Revenue'].sum()}")
