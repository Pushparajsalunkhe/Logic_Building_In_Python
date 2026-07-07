def name(n):
    for i in range (n):
        for j in range (i+1):
            if(j==0 or i==3 or i==j):
                print("*",end="")
            else:
                print(" ",end="")
        print()
name(6)