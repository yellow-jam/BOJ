a,b=0,0
x=[0,0,0]
y=[0,0,0]


for i in range(3):
    x[i],y[i]=map(int,input().split())

for i in range(3):
    a=x[i] if x.count(x[i])==1 else a
    b=y[i] if y.count(y[i])==1 else b

print(a,b)
