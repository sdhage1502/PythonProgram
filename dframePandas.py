import pandas as pd

data={
    'id':[1001,1002,1003],
    'name':['Tom','Nick','jhony'],
    'hra':[12000,13000,1100],
    'ta':[6000,5000,4000],
    'da':[10000,9000,8000]
    
}
df=pd.DataFrame(data)
print(df)
print(df.sum())
print("mean of the each  intgers column",df.select_dtypes(include='int64').mean())
print("median of the each integer column",df.select_dtypes(include='int64').median())
print("mean of the da column",df['da'].mean())
print("sum of the ta column",df['ta'].sum())