a, b=input().split()

A=int(a[2]+a[1]+a[0])
B=int(b[2]+b[1]+b[0])

print(A) if A>B else print(B)


# frank8711 님 코드
'''
a, b = input().split()
a = a[::-1]
b = b[::-1]
print(max(a, b))
'''
# 와 뒤집는걸 이렇게...! 잘 알아갑니다 
