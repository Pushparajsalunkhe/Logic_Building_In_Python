d={}
while True :
    k=eval(input('Enter the key'))
    v=eval(input('Enter the value'))
    d[k]=v
    choice=input('continue (y/n)')
    if choice=='n':
        break
print(d)
