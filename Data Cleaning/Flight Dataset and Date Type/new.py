import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('us-daily-passengers.csv')
print(df.head())
print(df.columns)
print(df.shape)
df['date'] = pd.to_datetime(
    df['date'],
    format='%m/%d/%y'
)
print(df.head())
df['day']=df['date'].dt.strftime('%a')
print(df.head())
temp=df.groupby('day')['num_passengers'].mean().reset_index()
print(temp.head(10))
plt.barh(temp['day'],temp['num_passengers'])
plt.show()