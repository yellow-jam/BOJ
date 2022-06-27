N=int(input())
n=N
count=0
while True:
    a10=n//10
    a1=n%10

    M=a10+a1

    n=a1*10+M%10
    count+=1
    if (N==n):
        break
print(count)
