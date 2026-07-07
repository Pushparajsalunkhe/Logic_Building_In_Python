n=int(input("Enter the Number"))
s=0
while(n!=0):
    r=n%10
    s+=r
    n//=10
print(f"count of digit ={s}")