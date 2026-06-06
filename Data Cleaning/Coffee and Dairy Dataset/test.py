import pandas as pd
df=pd.read_csv('coffee-survey-results.csv')
#print(df.head())
#print(df.columns)
sweet_1=[ 'What kind of sugar or sweetener? (Granulated Sugar)',
       'What kind of sugar or sweetener? (Artificial Sweetener)',
       'What kind of sugar or sweetener? (Honey)',
       'What kind of sugar or sweetener? (Maple Syrup)',
       'What kind of sugar or sweetener? (Stevia)',
       'What kind of sugar or sweetener? (Agave Nectar)',
       'What kind of sugar or sweetener? (Brown Sugar)',
       'What kind of sugar or sweetener? (Raw Sugar)']
sweet=df[sweet_1]
print(sweet.shape)
print(sweet.head())
print(sweet.isna())
sweet=sweet.dropna()
print(sweet.shape)
print(sweet.head(10))
ans=sweet.mean()*100

print(type(ans))
print(ans)
ans=ans.sort_values(ascending=True)
print(ans)
