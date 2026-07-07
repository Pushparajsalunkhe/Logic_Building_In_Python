def perfect(n):
    s=0
    for i in range (1,n):
        if n%i==0:
            s+=i

    if s==n:
        return True
    else:
        return False

a=int(input("Enter the number"))
if perfect(a):
    print(f"{a} is perfect number")
else:
    print(f"{a} is not perfect number")
