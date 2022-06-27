N=int(input())
F=int(input())

n=(N//100)*100
for i in range(n,n+100):
    if i%F==0:
        print("%02d"%(i%100))
        break
