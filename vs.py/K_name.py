for i in range (6):
    for j in range (6):
        if (j==0 or i==j+2  or i==4-j):
            print("*",end="")
        else :
            print(" ",end="")
    print()