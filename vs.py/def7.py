def sum_of_digit(n):
    s=0
    while n!=0:
        r=n%10
        s=s+r
        n//=10


    return s

a=int(input("enter the number"))
print(sum_of_digit(a))
