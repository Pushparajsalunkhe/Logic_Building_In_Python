for i in range (4):
    for j in range (6):
        if (j==0 or j==5 or i==j):
            print("*",end="")
        else :
            print(" ",end="")
    print()