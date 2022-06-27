ss=str(input())
res=[]
# print(ss.index('a'))

for i in range(97, 123, 1):
    try:
        res.append(str(ss.index(chr(i))))
        
    except:
        res.append('-1')
        
print(" ".join(res))
