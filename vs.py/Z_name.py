for i in range (5):
    for j in range (5):
        if(i==0 or i==4 or i==4-j):
            print("*",end="")
        else :
            print(" ",end="")
    print()