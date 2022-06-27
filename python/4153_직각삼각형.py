while True:
    length=list(map(int,input().split()))
    if sum(length)==0:
        break
    
    MAX=max(length)
    length.remove(MAX)
    if MAX**2==length[0]**2+length[1]**2:
        print("right")
    else: print("wrong")


#gtsdy0204 님 코드 베낀 셈이 됐다
