case=int(input())

for i in range(case):
    p=0
    k=0
    aa=list(map(int, input().split()))
    n=aa[0]
    del aa[0]
    ave=sum(aa)/n
    for j in range(n):
        if ave<aa[j]:
            k+=1
    p=k/n*100
    print("%.3f%%" %p)
