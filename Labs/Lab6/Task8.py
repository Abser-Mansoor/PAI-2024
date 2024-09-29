import pandas as pd

df1 = pd.read_csv('Products.csv')
df2 = pd.read_csv('Orders.csv')
print(df1.head(5))
print(df1.tail(10))
print("DataFrame two:\n")
print(df2.head(5))
print(df2.tail(10))
Merged = pd.merge(df1,df2,on='ProductID')
Merged['Revenue'] = Merged['Quantity'] * Merged['Price']
Sorted_Merged = Merged.sort_values(ascending=False,by='Revenue')
print(f"Top 5 Best Selling Products:\n{Sorted_Merged.head(4)}\n")
print(f"Top 5 Low Selling Products:\n{Sorted_Merged.tail(4)}\n")
print(f"Total Revenue is: {Merged['Revenue'].sum()}\n")
print(f"Most Common Best Seller: {Sorted_Merged.head(4).sort_values(by='Quantity',ascending=False)[:1]['ProductName']}\n")
average_by_category = Merged.groupby('Category')['Price'].mean().reset_index()
print(f"Average Prices of Each Category of Products\n\n{average_by_category}\n")
Merged['Order Date'] = pd.to_datetime(Merged['Order Date'],format = '%m-%d-%Y')
Merged['Year'] = Merged['Order Date'].dt.year
Merged['Month'] = Merged['Order Date'].dt.month
Merged['Day'] = Merged['Order Date'].dt.day
Revenue_by_day = Merged.groupby(['Year', 'Month','Day'])['Revenue'].sum().reset_index()
Revenue_by_month = Merged.groupby(['Year','Month'])['Revenue'].sum().reset_index()
Revenue_by_year = Merged.groupby(['Year'])['Revenue'].sum().reset_index()
print(f"Highest Revenue by Day\n\n{Revenue_by_day.loc[Revenue_by_day['Revenue'].idxmax()]}\n")
print(f"Highest Revenue by Month\n\n{Revenue_by_month.loc[Revenue_by_month['Revenue'].idxmax()]}\n")
print(f"Highest Revenue by Year\n\n{Revenue_by_year.loc[Revenue_by_year['Revenue'].idxmax()]}\n")
print(f"Total Revenue for Each Month\n\n{Revenue_by_month}\n")
print(f"Check for null values in Merged DataFrame:\n{Merged.isnull().sum()}")
Cleansed_Merged = Merged.dropna()
Cleansed_Merged = Cleansed_Merged[Cleansed_Merged['Quantity'].apply(lambda x: str(x).isdigit())]
Cleansed_Merged['Price'] = pd.to_numeric(Cleansed_Merged['Price'], errors='coerce')
print(f"Final Cleansed DataFrame\n\n{Cleansed_Merged}")
