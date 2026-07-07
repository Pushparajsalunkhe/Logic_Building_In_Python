for i in range (6):
    for j in range (6):
        if ( (i==0 and j==0) or (i==1 and j==0) or (i==2 and j==0) or (i==3 and j==0)or (i==0 and j==1) or (i==0 and j==2) or (i==0 and j==3) or (j==3 and i==1 ) or (j==3 and i==2) or (i==3 and j==1)or (j==2 and i==3) or (j==3 and i==3) or (j==4 and i==4) or (j==5 and i==5) or (j==2 and i==2) or (j==1 and i==1)):
            print("*",end="")
        else :
            print(" ",end="")
    print()