def prime(n):
    for i in range (2,n):
        if n%i==0:
            return False

        else:
            return True


a=int(input('Enter the number'))
if prime(a):
    print(f"{a} is prime number")
else:
    print(f"{a} is not prime number")