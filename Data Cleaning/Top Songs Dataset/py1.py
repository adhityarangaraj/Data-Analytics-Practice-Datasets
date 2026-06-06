import pandas as pd
df=pd.read_csv('top-song-durations.csv')
print(df.head())
temp=df['duration'].str.split(":",expand=True)
temp=temp.astype('int')
print(temp.head())
df[['h','m','s']]=temp
print(df.head())
temp=df.query('year>1968')
temp['total_secs']=temp.eval('(h*3600)+(m*60)+s')
print(temp['total_secs'].mean())
