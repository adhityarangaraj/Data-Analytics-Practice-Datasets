import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('extension_internet_users_by_continent.csv')
df1=pd.read_csv('extension_historical_population_by_continent.csv')
print(df.shape)
print(df1.shape)
print(df.head())
print(df1.head())
df1=df1[df1['year']>=1990]
df1=df1.dropna()
print(df1.head())
merged=pd.merge(df,df1,on=['year','continent'],how='left')
merged=merged.dropna()
print(merged.head())
merged['percent']=merged.eval('internet_users/population*100')
merged['percent']=merged['percent'].round(2)
print(merged.head())
print(merged['percent'].max())
#For Asia
#print(type(df.query('year==1990')))
asia=merged.query('continent== "Asia"')
print(asia.head())
print(asia.query('percent >=50'))
#So asia got 50% of population in year 2020
