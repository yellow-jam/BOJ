ss=list(map(int,input().split()))
ss.remove(max(ss))
ss.remove(min(ss))
print(ss[0])
