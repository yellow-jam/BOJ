#유사 하드코딩함...

MAX=123456

is_prime = [True for i in range(MAX*2+1)]
is_prime[1] = False
for i in range(1, int((MAX*2) ** 0.5) + 1):
    if(is_prime[i]):
        for j in range(i * i, MAX*2 + 1, i):
            is_prime[j] = False
            

n=int(input())


while (n!=0):

    print(is_prime[n+1:2*n+1].count(True))


    n=int(input())
