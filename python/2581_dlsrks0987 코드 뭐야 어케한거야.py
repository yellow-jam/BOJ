import math

M = int(input())
N = int(input())
array = [True for i in range(N+1)]
for i in range(2, int(math.sqrt(N))+1):
    if array[i] == True:
        j=2
        while i*j <= N:
            array[i*j] = False
            j+=1

count=0
sm = 0
if M==1:
    array[1] = 10001
for i in range(M, N+1):
    if array[i] == True:
        array[i]=i
        sm += i
        count+=1
    else:
        array[i] =10001

if count ==0:
    print(-1)
else:

    print(sm, min(array[M:]), sep='\n')


#결과: 메모리 31312 시간 80
#내 결과: 메모리 29200 시간 1084
