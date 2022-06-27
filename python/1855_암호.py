import sys

K = int(sys.stdin.readline().rstrip())

str = sys.stdin.readline().rstrip()

array=['' for i in range(K)]
print(array)

k=0
for i in str:
    array[k]+=i
    k+=1
    if k==K: k=0

res=''
for i in array:
    res+=i
print(res)