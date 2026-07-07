import pandas as pd
import numpy as np
from sklearn import linear_model
df=pd.read_csv(r"C:\Users\patil\OneDrive\Documents\multipal.csv")
print(df)
a=df.bedrooms.median()
print(a)
import math
median_bedrooms=math.floor(df.bedrooms.median())
print(median_bedrooms)
df.bedrooms=df.bedrooms.fillna(median_bedrooms)
print(df)
reg=linear_model.LinearRegression()
print(reg)
b=reg.fit(df[['area','bedrooms','age']],df.price)
print(b)
print(reg.coef_)
print(reg.intercept_)
print(reg.predict([[450,2,8]]))
print(137.25*3000+-26025*3+-6825*40+383724.9999999998)
