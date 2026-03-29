import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data={
    'product':['laptop','tv','mobile','milk','veg','grains'],
    'price':[1000,467,675,65,65,54],
    'quantity':[2,5,6,1,6,2],
    'category':['electronic','electronic','electronic','dairy','veg','grains']

}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())
print(df.shape)
print(df.isnull().sum())
print(df.describe())
print(df.fillna(0))
df['total_sales']=df['quantity']*df['price']
print(df['total_sales'].sum())
print(df.groupby('category')['total_sales'].sum())
plt.hist(df)
plt.show()
