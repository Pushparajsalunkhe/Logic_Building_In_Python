import pandas as pd 
df=pd.read_csv(r"C:\Users\patil\Desktop\pushparaj.pa.csv")
print (df)
a=df.dtypes
print(a)
b=df.head()
print(b)
c=df.tail()
print(c)
s=df.describe()
print(s)
e=df.info()
print(e)
p=df.dtypes=="object"
print(p)