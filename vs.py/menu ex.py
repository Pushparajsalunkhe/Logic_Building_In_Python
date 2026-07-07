while True:
    print("\n \n !!!! MANU !!!! \
        \n1.Addition\
        \n2.Subtaction\
        \n3.Multipication\
        \n4.Division\
        \n5.Power\
        \n0.exit")
    choice=int(input("Enter your choice "))
    if(choice==0):
        print("Good Bye")
        break
    if(choice>=1 and choice<=5):
        a=int(input("Enter First Number"))
        b=int(input("Enter Second Number"))
        if(choice==1):
            print(f"Addition={a+b}")
        elif(choice==2):
             print(f"Subtection={a-b}")
        elif(choice==3):
             print(f"Multipication={a*b}")
        elif(choice==4):
             print(f"Division={a/b}")
        else:
            print(f"power={a**b}")
    else:
        print("Invalid choice")
        

    