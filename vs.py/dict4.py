d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
out=d1.copy()
out.update(d2)
out.update(d3)
print(out)

#best methode
a={**d1,**d2,**d3}
print(a)