import itertools as itr 
n=int(input("Enter the number:"))
coca=['','','coca']
coca_cycle=itr.cycle(coca)
cola=['','','','','cola']
cola_cycle=itr.cycle(cola)
cocacola=(x+y for x,y in zip(coca_cycle,cola_cycle))
for s in itr.islice(cocacola,n):
    print(s)