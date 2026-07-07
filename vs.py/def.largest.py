def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else :
        return c
print('Enter the three number',end='')
x,y,z=[int(i) for i in input().split()]
print(largest(x,y,z))