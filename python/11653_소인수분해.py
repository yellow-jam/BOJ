N=int(input())
n=N

for i in range(2,N+1):
    while n%i==0:
        print(i)
        n=n//i
        
