# 1, 2(6개), 3(12개), 4(18개)
'''
n=int(input())
count=0
cycle=1
if n>1:
    while count<n:
        for i in range (cycle*6):
            count+=1
            if count==n:
                break
        cycle+=1
print(cycle)
'''


n=int(input())
k=0
if n>1:
    while ((n-1)/6) > (k*(k+1)/2):
        k+=1
print(k+1)
