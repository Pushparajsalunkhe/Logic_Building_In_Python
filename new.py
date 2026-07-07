num=12
n=num
total=0
op=len(str(n))
while num >0:
    new=num%10
    total=total+(new**op)
    num=num//10
if n==total:
    print("A")
else:
    print("not")