score=0
total=0

n=int(input())

for i in range(n):
    ss=input()
    for char in ss:
        if char=='O':
            score+=1
            total+=score
        else:
            score=0
    print(total)
    score=0
    total=0
