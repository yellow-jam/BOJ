

M=int(input())
N=int(input())

aa=[]

for i in range(M,N+1):

    if i<2:
        continue
    elif i==2:
        aa.append(2)
    elif i>2:  
        for j in range(2, i):
            if i%j==0:
                break
            elif j==i-1:
                aa.append(i)

if aa==[]:
    print(-1)
else:          
    print(sum(aa))
    print(min(aa))


#조건문이 너무 많이 달렸어
