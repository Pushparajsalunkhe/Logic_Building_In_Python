from datetime import date 
import math 
print("Enter the day,month,year")
d,m,y=[int(x) for x in input().split()]
dob=date(y,m,d)
td=date.today()
age=(td-dob).days/365.25
print(age)