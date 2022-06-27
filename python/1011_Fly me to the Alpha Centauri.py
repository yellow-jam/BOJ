
def year(dis):

    if dis==1:
        return 1
    elif dis==2:
        return 2
    else:
        move=2
        count=2
        for i in range(2,2+dis):
            move+=i
            count+=1
            if dis<=move: return count
            move+=i
            count+=1
            if dis<=move: return count


test=int(input())

for i in range(test):
    x,y=map(int,(input().split()))
    print(year(y-x))
