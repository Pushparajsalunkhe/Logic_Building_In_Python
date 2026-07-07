while True:
    n=int(input("Enter the number"))
    i=1
    while(i<n):
        if(n%2==0):
            break
        i+=1
    if(i==n):
        print(f"{n} is prime number")
    else:
        print(f"{n} is not prime number")
        choice=input("contiuse y/n")
        if(choice=="n"):
            break

