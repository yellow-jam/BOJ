import sys


aa=[]
n=int(sys.stdin.readline())
for i in range(n):
    aa.append(n-i)

while (len(aa)>1):
    aa.pop()
    aa.insert(0,aa.pop())

print(aa[0])


#자꾸 시간 초과됨 내 수준에서는 안 되는 건가?
