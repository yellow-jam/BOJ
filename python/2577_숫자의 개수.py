b=0
c=[0,0,0,0,0,0,0,0,0,0]
n=int(input())
n=n*int(input())
n=n*int(input())

while True:
    b=n%10
    c[b]+=1
    n=n//10
    if n==0:
        break

for i in range(10):
    print(c[i])


# cubar1s 의 코드
'''
a= int(input())
b= int(input())
c= int(input())
l=list(str(a*b*c))
for i in range(10):
    print(l.count(str(i)))

'''
