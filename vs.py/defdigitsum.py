def digit(n):
    s=0
    while n!=0:
        r=n%10
        s=s+r
        n//=10


    return s

x=int(input("enter the digit"))
print(digit(x))

#point values calculation
def digit1(n):
    g=str(n)
    s=0
    for i in g:
        if i.isdigit():
            s=s+int(i)


    return s

x=eval(input("Enter the digit:"))
print(digit1(x))   