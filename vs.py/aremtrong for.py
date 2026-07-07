for n in range(100,501):
    s=0
    t=n
    while(n!=0):
        r=n%10
        s=s+r**3
        n//=10
    if s==t:
        print(f'{t} is aramtrong number')