#학생 분류하기
def student():
    a,b=map(int,input().split())
    if a==1:
        남학생(b)
    elif a==2:
        여학생(b)

#남학생 함수
def 남학생(n):
    global length
    for i in range(n-1,length,n):
        condition[i]=not condition[i]

#여학생 함수
def 여학생(n):
    n=n-1
    global length
    condition[n]=not condition[n]
    i=1
    while n+i<length and n-i>=0:
        if condition[n+i]==condition[n-i]:
            condition[n+i]=not condition[n+i]
            condition[n-i]=not condition[n-i]
        i+=1

#출력하기
def result(aa):
    for i in range(1,len(aa)+1):
        print(aa[i-1], end=' ')
        if i%20==0:
            print()


## 메인 함수 ##
'''
#입력 받기
global length
length=int(input("스위치 수:"))

global condition
condition=list(map(bool, map(int,input("스위치 상태:").split())))

N=int(input("학생 수:"))
for i in range(N):
    student()

condition=list(map(int,condition))
result(condition)
'''


#result([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5])


global length
length=8
global condition
condition=list(map(bool, map(int,[0,1,0,1,0,0,0,1])))

남학생(3)
여학생(3)
condition=list(map(int,condition))
result(condition)

