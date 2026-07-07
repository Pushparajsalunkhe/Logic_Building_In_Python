for i in range (4):
    for j in range (4):
        if(j==0 or j==3 or i==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()