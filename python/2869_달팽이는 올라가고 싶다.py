import math

A,B,V=map(int,input().split())

n=math.ceil((V-A)/(A-B))+1

print(n)
