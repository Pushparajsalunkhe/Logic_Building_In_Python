def evan(n):
    for i in n:
        if i%2==0:
            print(i,end="\t")

s=eval(input("Enter the list [] :"))
evan(s)