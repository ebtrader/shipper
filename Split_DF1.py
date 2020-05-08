import pandas as pd
from usps import USPSApi

df = pd.DataFrame({'Tracking Number':['10X4R3W','30X5R3W','9410808205497580311496','9410808205497580311496','9410808205497580311496'], 'A':[3,4,7,6,1], 'Shipper':['Fedex', 'Fedex', 'USPS', 'USPS', 'USPS']})
print (df)

s = 30

#df1 = df[df['Sales'] >= s]
df1 = df[df['Shipper'] == 'Fedex']
df2 = df[df['Shipper'] == 'USPS']


print(df1)
print ()
print(df2)
print ()

for i in df2['Tracking Number']:
    usps = USPSApi('107GOFAS1661')
    # sample tracking number 9410808205497580311496

    track = usps.track(i)

    print(track.result)
