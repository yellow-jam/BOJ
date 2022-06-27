import math

def is_prime(n):
    if n==1: return False
    end=int(math.sqrt(n))
    for i in range(2,end+1):
        if n%i==0:
            return False
    return True


a,b=map(int,input().split())

for i in range(a,b+1):
    if is_prime(i):
        print(i)

#출처: https://yongku.tistory.com/entry/백준-알고리즘-백준-1929번-소수-구하기-파이썬Python [츄르 사려고 코딩하는 집사]
