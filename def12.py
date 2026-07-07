import itertools as itr 
s1=eval(input('Enter the list1:'))
s2=eval(input("Enter the list:"))
c=[x+y for x,y in itr.zip_longest(s1,s2,fillvalue=0)]
    
print(c)