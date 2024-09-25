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
Sorted_Merged = Merged.sort_values(ascending=False,by='Revenue')
print(f"\nTop 5 Best Selling Products:\n{Sorted_Merged.head(4)}\n")
print(f"\nTop 5 Low Selling Products:\n{Sorted_Merged.tail(4)}\n")
print(f"\nTotal Revenue is: {Merged['Revenue'].sum()}\n")
print(f"\nMost Common Best Seller: {Sorted_Merged.head(4).sort_values(by='Quantity',ascending=False)[:1]['ProductName']}\n")
average_by_category = Merged.groupby('Category')['Price'].mean().reset_index()
