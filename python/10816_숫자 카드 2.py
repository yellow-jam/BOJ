import sys

N = int(sys.stdin.readline())
n_array = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
m_array = list(map(int, sys.stdin.readline().split()))

res = [0 for i in range(M)]

# 상근이가 가진 카드를 루프로 돌리면서

for i in n_array:
    if i in m_array:
        res[m_array.index(i)] += 1

# 대조해서 있으면 res[인덱스]에 +1
for i in range(M):
    print(res[i], end=" ")