a,b=map(int,input().split())
G,L=1,1

for i in range(2, min(a,b)+1):
        while a%i==0 and b%i==0:
            a=a//i
            b=b//i
            G=G*i
L=a*b*G
print(G)
print(L)
