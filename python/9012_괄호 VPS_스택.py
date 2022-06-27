# 스택

# 왼쪽괄호면 +1
# 오른쪽괄호면 -1
# 이때 수가 -1이 되면 break

def check(str):
    check = 1
    for i in range(len(str)):
        if(str[i]=='('):
            check+=1
        else:
            check-=1

        if (check==0):
            return "NO"

    if (check == 1):
        return "YES"
    return "NO"

## 메인 ##
import sys

N=int(sys.stdin.readline().strip())

for i in range(N):
    str = sys.stdin.readline().strip()
    print(check(str))




'''
for i in range(N):
    check = 1
    str=sys.stdin.readline().strip()
    for j in range(len(str)):
        if(str[j]=='('):
            check+=1
        else:
            check-=1

        if (check==0):
            print("NO")
            break
    if (check != 1):
        print("NO")
        continue
    print("YES")
'''
