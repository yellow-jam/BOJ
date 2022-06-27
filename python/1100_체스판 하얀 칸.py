

count=0
for i in range(8):
    ss=input()
    for j in range(8):
        if ss[j]=='F':
            if i%2==0 and j%2==0: count+=1
            elif i%2==1 and j%2==1: count+=1
print(count)
