m,n=map(int,input().split());l=[*range(n+1)]
for i in l:
 if 1<i:l[i*i::i]=-(i+~n//i)*[0]   # ~가 무슨 뜻이지 비트 not 연산자인듯한데
 #연산속도 줄이려고 이러나 비트연산<십진연산일테니까...
 if 1<i>=m:print(i)
