import operator as op
d=eval(input('Entre the dict{}'))
print("pair in assending order")
print(sorted(d.items(),key=op.itemgetter(1)))

print("pair in disending order")
print(sorted(d.items(),key=op.itemgetter(1),reverse=True))