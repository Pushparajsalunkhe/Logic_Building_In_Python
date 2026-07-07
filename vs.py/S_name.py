for i in range (4):
    for j in range (4):
        if(i==0 or j==0 or i==3):
            print("*",end="")
        else :
            print(" ",end="")
    print()
for k in range (3):
    for p in range (4):
        if (p==3 or k==2):
            print("*",end="")
        else :
            print (" ",end="")
    print()