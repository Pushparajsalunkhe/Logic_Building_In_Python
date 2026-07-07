num=121
a=num
l=len(str(num))
s=0
n=0
while num>=0:
    s=num%10
    n=s**l
    num//=10
if n==a:
    print("a") 
else:
    print("not a")



