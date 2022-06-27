n=int(input())
k=1
if n>1:
    while n > (k*(k+1)/2):
        k+=1

a=n-(k*(k-1)/2)
b=k+1-a

if k%2!=0:
    a,b=b,a

print("%d/%d"%(a, b))


# socce12 님 코드 가독성 좋다
'''
num = int(input())
i = 1

while num - i > 0:  # 아 이런 방법이
    num -= i
    i += 1

if i % 2 == 0:
    print(f"{num}/{i-num+1}")
else:
    print(f"{i-num+1}/{num}")
'''
