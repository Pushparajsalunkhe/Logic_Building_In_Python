q=[]
while True:
    print("\n\n")
    print("!!!! MANU !!!! \
        \n1.insert\
        \n2.deleta\
        \n3.display\
        \n4.clear\
        \n0.exit")
    choice=int(input('Enter the choice'))
    if choice==0:
        
        print("Good bye")
        break
    if choice==1:
        a=int(input("Enter the number"))
        q.append(a)
        print(f"{a} is insert noto the Queue")
    elif choice==2:
        if not q:
            print("Queue is empty")
            continue
        p=q.pop(0)
        print(f"{p} is deleta noto the queue")
    elif choice==3:
        if not q:
            print("Queue is empty")
            continue
        for i in q:
            print(i,end='\t')
    elif choice==4:
        if not q:
            print("Queue is empty")
            continue
        q.clear()
        print("queue is clear")
    else:
        print("invalid choice")
        