def get_number(n):
    s=[]
    for ch in n:
        if type(ch) in (int,float):
            s.append(ch)

    return s


a=eval(input('Enter the list'))
print(get_number(a))