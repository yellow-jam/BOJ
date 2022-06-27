N,M=map(int,input().split())

#2차원 배열 -> 실행시간 너무 길 것 같은데
array=[]
for i in range(N):
    array.append(input())

sqr=[1]
for i in range(1,min(N,M)+1):
    for n in range(N-i):
        for m in range(M-i):
            if array[n][m]==array[n+i][m]==array[n][m+i]==array[n+i][m+i]:
                sqr.append(i+1)
                break

print(max(sqr)**2)
