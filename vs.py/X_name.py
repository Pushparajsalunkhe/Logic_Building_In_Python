for i in range (5):
    for j in range (5):
        if(i==j or i==4-j):
            print("*",end="")
        else :
            print(" ",end="")
    print()