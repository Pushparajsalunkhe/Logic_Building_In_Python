for i in range (4):
    for j in range (4):
        if(j==0 or j==3 or i==0 or i==3 ):
            print("*",end="")
        else :
            print(" ",end="")
    print()
for k in range (3):
    for p in range (4):
        if(p==0 or p==k+1):
            print("*",end="")
        else :
            print(" ",end="")
    print()