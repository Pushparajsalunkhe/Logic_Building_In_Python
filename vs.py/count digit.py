n=int(input("Enter The Number"))
d=int(input("Enter The Digit"))
c=0
while(n!=0):
    r=n%10
    if(r==d):
        c+=1
    n//=10
print(f"{d} Occuring in {c} Time ")