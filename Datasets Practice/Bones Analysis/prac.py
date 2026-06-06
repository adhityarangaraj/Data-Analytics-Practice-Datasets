import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('bird-neck-bones.csv')
#print(df.shape)
#print(df.head())
#print(dir(df))

#Which bird has the fewest neck vertebra?
#Find the row with the minimum number of neck vertebrae.
temp=df.query('neck_vertebrae == neck_vertebrae.min()')
print(temp)
#Do humans have more bones in the arms or legs?
df1=pd.read_csv('adult-human-skeleton.csv')
print(type(df1['region'].value_counts()))
temp=df1['region'].value_counts()
#Sort the df based on fusion form
print(temp[['arm','leg']].idxmax())
print(type(df1.sort_values(by='fused_from')))
da=(df1.sort_values(by='fused_from'))
#How many ribs to humans have?
temp1=df1['name'].value_counts()
print(temp1)
print(df1['name'].str.contains('rib',case=False).sum())
