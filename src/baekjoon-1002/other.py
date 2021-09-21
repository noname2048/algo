T=int(input())
import sys
num=sys.stdin.readlines()
for i in num:
    x1,y1,r1,x2,y2,r2=map(int,i.split())
    dist=(((x1-x2)**2)+((y1-y2)**2))**0.5
    if dist>r1+r2: print(0)
    elif dist==r1+r2: print(1)
    elif abs(r1-r2)<dist<r1+r2:print(2)
    elif abs(r2-r1)==dist and r2==r1: print(-1)
    elif abs(r2-r1)==dist: print(1)
    else: print(0)
