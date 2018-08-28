from random import randint
from math import *

def factor(r):
    t = r
    z = t**(1/2)
    p = z%1
    f = []
    e = 3
    s = 2
    q = int(t/2) + 1
    if t%2 == 0:
        e = 2
        s = 1
    if p != 0:
        y = floor(z)
    else:
        y = int(z) + 1
    for j in range(e,y,s):
        d = (t/j);
        if (t%j) != 0:
            continue
        for k in range(e,q,s):
            if j*k == t:
                h = [j,k]
                f.append(h)
                break
    if not f:
        f.append([t])

    else:
        f.append([t])
    return f

c1 = 0
c2 = 0
c3 = 0
g = 100000000
s = 3

for i in range(1,s+1):
    a = list(set([item for sublist in factor(randint(1,g)) for item in sublist]))
    b = list(set([item for sublist in factor(randint(1,g)) for item in sublist]))
    c = []
    c1 += 1
    for bx in b:
        if bx in a:
            c.append(bx)
            
    if c:
        #print "these are the elements of list a that are present in list b:"
        #(c)
        c2 += 1
    else:
        #print "no elements of list a are in list b"
        c3 += 1
        pass
    print((((c1)/s)*100),"%",sqrt(6/(c3/c1)),"pi approx.")
    #if (((c1)/s)*1000)%10 == 0:
        #print(round(((c1)/s)*100),"%",sqrt(6/(c3/c1)),"pi approx.")
print("Complete")
print(c1,"outcomes")
print(c2,"unfavourable outcomes")
print(c3,"favourable outcomes")
print(sqrt(6/(c3/c1)),"pi approx.")
