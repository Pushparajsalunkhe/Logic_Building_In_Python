print("!!! MANU !!!")
print(f"1.Addition \
    \n2.subtraction \
    \n3.Multiplication \
    \n4.Division \
    \n5.Power")
ch=int(input("Enter the choice"))
if(1<=ch<=5 ):
    a=eval(input('Enter the first number'))
    b=eval(input("Enter the second number"))
    if(ch==1):
        print(f"Addition ={a+b}")
    elif(ch==2):
        print(f"Subtection ={a-b}")
    elif(ch==3):
        print(f"multipication ={a*b}")
    elif(n==4):
        print(f"Divistion ={a/b}")
    else:
        print(f"Power ={a**b}")
else:
    print("Invalid choice")