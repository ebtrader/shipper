import pandas as pd

df = pd.DataFrame({'Sales':[10,20,30,40,50], 'A':[3,4,7,6,1], 'Shipper':['Fedex', 'Fedex', 'UPS', 'UPS', 'Conway']})
print (df)

s = 30

#df1 = df[df['Sales'] >= s]
df1 = df[df['Shipper'] == 'Fedex']

print(df1)
