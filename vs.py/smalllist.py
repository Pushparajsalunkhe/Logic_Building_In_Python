a=eval(input("Enter the list"))
m=a[0]
for i in a:
    if i < m:
        m=i
print(m)