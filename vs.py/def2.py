def dummy():
    x=10       #local variabel
    print(x)
    print(a)

a=20  # global variabel
dummy()
print(a) #only print global variabel not local in give error