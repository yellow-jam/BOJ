def d(n):
    x=0
    a=list(str(n))
    for i in a:
        x=x+int(i)
    return n+x

exist=set([d(n) for n in range(10000)])
N=set(range(10000))

new=N-exist
for i in sorted(new):
    print(i)

''' 개오래걸리는 코드
for i in range(10000):
    if i in exist:
        continue
    else:
        print(i)
'''
        
# 와 qmffndkzm 이사람 똑똑이
# list(str(n)), 세트 차집합(-)연산
# 이사람 84ms 걸림;; 나는 고친 최종본도 96ms 걸리는구만

'''
def d(n):
    x = 0
    a = list(str(n))
    for i in a:
        x = x + int(i)
    return n+x

s_set = set()
for k in range(1,10000):
    s_set.add(d(k))
ans = set(range(1,10000)) - s_set
for num in sorted(ans):
    print(num)
'''
