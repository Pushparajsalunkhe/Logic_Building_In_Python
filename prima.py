n=int(input("Enter the number"))
i=1
c=0
while(i<=n):
    if(n%i==0):
        c+=1
    i+=1
if(c==2):
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")
        
