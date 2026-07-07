stack=[]
while True:
    print("\n\n")
    print("!!!! MANU !!!! \
        \n1.push \
        \n2.pop\
        \n3.display\
        \n4.clear\
        \n0.exit")
    choice=int(input("Enter the choice :"))
    if choice==0:
        print("Good Bye")
        break
    if choice==1: #push element
        a=int(input('Enter the element'))
        stack.append(a)
        print(f'{a} is push onto the stack')
    elif choice==2: #pop element
        if not stack:
            print("stack is empty")
            continue
        x=stack.pop()
        print(f"{x} is pop onto the stack")
    elif choice==3:  #display
        if not stack:
            print("stack is empty")
            continue
        for i in stack[::-1]:
            print(i)
    elif choice==4: #clear stack
        if not stack:
            print("stack is empty")
            continue
        stack.clear()
        print("stack is cleared")
    else:
        print("Invalid choice")