T=int(input())

if T%10!=0:
    print(-1)

else:
    m5=T//300
    T=T%300
    m1=T//60
    T=T%60
    s10=T//10

    print(m5,m1,s10)
