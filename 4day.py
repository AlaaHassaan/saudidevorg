y=1 #int
x=6.9 #float
v=1j #complex
print(type(y))
print(type(x))
print(type(v))

#int type example
t=7
g=9876543456
k=-55667
print(type(t))
print(type(g))
print(type(k))
#float type example
c=1.10
d=9.0
f=-5.77
print(type(c))
print(type(d))
print(type(f))

#float numbers with power of 10

b=44e4
h=9E3
l=-5.7e100
print(type(b))
print(type(h))
print(type(l))

#complex type example
z=7+7j
i=9j
r=-5j
print(type(z))
print(type(i))
print(type(r))

u=1   #int
n=2.6 #float
a=5j  #complex

#convert from int to float
w=float(u)
#convert from float to int
q=int(n)
#convert from int to complex
m=complex(u)
print(w)
print(q)
print(m)

print(type(w))
print(type(q))
print(type(m))

import random 
print(random.randrange(1,10))