import pandas as pd

df = pd.DataFrame({'Tracking Number':['10X4R3W','30X5R3W','20X6R3W','70X4R3W','80X7R3W'], 'A':[3,4,7,6,1], 'Shipper':['Fedex', 'Fedex', 'UPS', 'UPS', 'Conway']})
print (df)

s = 30

#df1 = df[df['Sales'] >= s]
df1 = df[df['Shipper'] == 'Fedex']
df2 = df[df['Shipper'] == 'UPS']
df3 = df[df['Shipper'] == 'Conway']

print(df1)
print ()
print(df2)
print ()
print(df3)
print ()

