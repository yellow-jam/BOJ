
ss=input().upper()
res=[]
for n in range(65, 91, 1):
    res.append(ss.count(chr(n)))

if res.count(max(res))>1:
    ans='?'

else:
    ans=chr(res.index(max(res))+65)
            
print(ans)

# 헐 ㅋㅋㅋ 코드 개더러울줄 알았는데 실행속도는 빠른축임...
