N=int(input())

n5=N//5
r=N%5 #나머지

while r%3!=0:
    n5=n5-1
    r=r+5
    if n5<0:
        break
n3=r//3

res=-1 if n5<0 else n5+n3
res=N//3 if (res==-1 and N%3==0) else res

print(res)


# gkqls813 님 코드
# 3씩 빼가면서 5로 처음 나눠떨어지는 순간을 찾기
'''
def salt(N):
    for i in range(N,-1,-3):
        if i%5==0:
            return i//5+(N-i)//3
    return -1
print(salt(int(input())))
'''
