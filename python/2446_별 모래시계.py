n=int(input())


for i in range (1, 2*n):
    print(" "*(i-1)+"*"*(2*n+1-2*i)) if i<n else print(" "*(2*n-1-i)+"*"*(2*(i-n)+1))


# 아예 윗부분 아랫부분 나눠서 조건식 판별 없이 반복문만 두 번 돌리는 게 빠름
