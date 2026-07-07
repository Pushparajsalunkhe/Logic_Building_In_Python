n=int(input("Enter the number"))
d={}
for i in range(1,n+1):
    d[i]=i*i
print(d)
#comprehesion
e={i:i*i for i in range(1,n+1)}
print(e)