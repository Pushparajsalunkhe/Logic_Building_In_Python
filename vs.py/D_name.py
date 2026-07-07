for i in range (6):
    for j in range (6):
        if(j==5 or i==0 or i==5 or j==1 ):
            print("*",end="")
        else :
            print(" ",end="")
    print()