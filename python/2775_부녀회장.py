import sys

array=[[]]

for i in range(1,16):
    array[0].append(i)

for i in range(1,15):
    array.append([])
    res=0
    for j in range(0, 15):
        res+=array[i-1][j]
        array[i].append(res)

N = int(sys.stdin.readline())
for i in range(N):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    print(array[a][b-1])

'''
k와 n이 1과 14 사이였구나... 배열을 만들기로 결심함 ↑

재귀 알고리즘은... 이런 계산에 적합하진 않겠죠...

def f(a, b):
    if (b==0): return 0
    if (a==0): return b
    return f(a-1,b)+f(a,b-1)

N = int(sys.stdin.readline())

for i in range(N):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    print(f(a,b))

'''


'''
문제 잘못 이해함
층 기준으로 왼쪽 아래 네모박스 전부 더해야하는줄

def f(a, b):
    if (b==0): return 0
    if (a==0): return b
    return f(a,b-1) + sum_vertical(a-1, b)

def sum_vertical(a, b):
    res=0
    for i in range(0,a+1):
        res += f(i, b)
    return res

N = int(sys.stdin.readline())
for i in range(N):
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    print(f(a,b))
    
'''
