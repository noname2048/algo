from math import*
for l in [*open(0)][1:]: 
    print(comb(*map(int,l.split()[::-1])))
