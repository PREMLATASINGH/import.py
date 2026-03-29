import numpy as np
import pandas as pd
data={
    'product':['laptop','tv','mobile','milk','veg','grains'],
    'price':[1000,467,675,65,65,54]

}
df=pd.DataFrame(data)
print(df)
print(df.head())
print(df.tail())