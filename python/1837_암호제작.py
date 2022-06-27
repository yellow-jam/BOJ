import math

p,k=map(int,input().split())

for r in range(2,int(math.sqrt(p))+1):
    if p%r==0:
        print("BAD",r) if r<k else print("GOOD")
        break
        
