case=int(input())
for i in range(case):
    res=''
    n,ss=input().split()
    for char in ss:
        for j in range (int(n)):
            res+=char
    print(res)


# yeejesijack 의 코드
'''
T = int(input())
for i in range(T):
    R, S = input().split()
    for k in S: 
        print(k*int(R), end='')
    print()
'''
