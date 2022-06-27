import sys

stack=[]  # 스택
ascend = 1  # 오름차순
answer = ""
flag = 0

N=int(sys.stdin.readline().strip())

for i in range(N):
    num = int(sys.stdin.readline().strip())
    while num>=ascend:
        stack.append(ascend)
        answer += "+\n"
        ascend += 1
    if (num==stack[-1]):
        stack.pop()
        answer += "-\n"
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    print(answer.strip())

# https://hongcoding.tistory.com/39
# 새 값이 들어올 때마다 검사, flag 사용

# C, C++
# https://cocoon1787.tistory.com/231