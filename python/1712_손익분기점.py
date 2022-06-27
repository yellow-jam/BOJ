import sys

A,B,C=map(int, sys.stdin.readline().split())
n=((A/(C-B))//1)+1 if C>B else -1 #A+B*n<C*n 인 정수 n 최솟값
print("%d"%n) if n>0 else print('-1')
