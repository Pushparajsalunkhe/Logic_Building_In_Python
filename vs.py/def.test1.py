def add (a,b):
    return a+b

def sub (a,b):
    return a-b

def mul (a,b):
    return a*b

def div (a,b):
    return a/b

switch={1:add,2:sub,3:mul,4:div}


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
        print("Enter Two number")
        x,y=[int(i) for i in input().split()]
        print(f'result=',switch.get(choice)(x,y))

    else:
        print("Invalid choice")