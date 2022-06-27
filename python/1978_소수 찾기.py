
n=int(input())
aa=list(map(int,input().split()))
count=0

for i in aa:

    if i<2:
        continue
    elif i==2:
        count+=1
    elif i>2:  
        for j in range(2, i):
            if i%j==0:
                break
            elif j==i-1:
                count+=1
            
print(count)
