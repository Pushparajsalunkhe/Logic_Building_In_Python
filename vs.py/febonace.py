while True:
    n=int(input("Enter the number"))
    x=0
    y=1
    print(x,y,end="\t")
    for i in range (n-2):
        z=x+y
        print(z,end="\t")
        x=y
        y=z
    ch=input("\nexit yes or no y/n")
    if ch=='n':
        break