n=int(input("Enter the number"))
i=1
s=0
while(i<n):
    if(n%i==0):
        s=s+i
    i+=1
if(n==s):
    print(f"{n} is Perfect Number")
else:
    print(f"{n} is Not Perfect Number")