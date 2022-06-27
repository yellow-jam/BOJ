import sys

N=int(sys.stdin.readline())
A=list(map(int, sys.stdin.readline().split()))

M=int(sys.stdin.readline())
B=list(map(int, sys.stdin.readline().split()))
for i in B:
    print(1) if i in A else print(0)
