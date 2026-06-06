import pandas as pd
df=pd.read_csv('first-day-of-week.csv')
print(df.head())
print(df.columns)
print(df.shape)
temp=df['first_day'].value_counts()
print(type(temp))
print(temp.sum())
df1=pd.read_csv('population.csv')
print(df1.head())
merged=pd.merge(df,df1,on='alpha3',how='left')
print(merged.head())
merged=merged.dropna()
print(merged.head())
print(merged['population'].sum())
df2=pd.read_csv('four-regions.csv')
print(df2.head())
merged=pd.merge(merged,df2,on='alpha3',how='left')
print(merged.head())
merged=pd.get_dummies(merged,columns=['first_day'])
print(merged.head())
temp=merged.groupby('four_regions')
temp=temp[['first_day_mon','first_day_sun','first_day_sat','first_day_fri']].sum().reset_index()
print(temp.head())
ind=temp['first_day_mon'].idxmax()
print(type(temp))
print(temp.iloc[ind,0])
print(temp[['first_day_mon',
      'first_day_sun',
      'first_day_sat',
      'first_day_fri']].idxmax(axis=1))


