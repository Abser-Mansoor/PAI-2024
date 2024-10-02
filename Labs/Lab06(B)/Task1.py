import pandas as pd

df1 = pd.read_csv('heart.csv')
print(df1['cp'].unique())
df1 = df1.rename(columns={'sex':'Gender'})
df1['Gender'][df1['Gender'] == 0] = 'Female'
df1['Gender'][df1['Gender'] == 1] = 'Male'
print(df1)

#Single grp
df = df1.groupby('Gender')
#Single col
print(df['chol'].max())
print(df['chol'].mean())
print(df['chol'].min())

#Single grp
dff = df1.groupby('Gender')
#Multiple col
print(dff[['chol','oldpeak','restecg']].max())
print(dff[['chol','oldpeak','restecg']].mean())
print(dff[['chol','oldpeak','restecg']].min())


