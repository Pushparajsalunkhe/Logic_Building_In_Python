def add (a,b):
    return a+b

def sub (a,b):
    return a-b

def mul (a,b):
    return a*b

def div (a,b):
    return a/b


while True:
    print("-"*30)
    print(f'1.Addition \
        \n2.Subtraction\
        \n 3.Multiplication\
        \n4.Divition\
        \n0.Exit')
    choice=int(input('Enter the choice'))
    if choice==0:
        print("Good Bye")
        break
    if choice in range(1,5):
        print("Enter two number")
        x,y=[int(i)for i in input().split()]
        if choice==1:
            print(f"Addition ={add(x,y)}")
        elif choice==2:
            print(f"subtraction={sub(x,y)}")
        elif choice==3:
            print(f"multiplication={mul(x,y)}")
        else:
            print(f"division={div(x,y)}")
    else:
        print("Invalid choice")