while True:
    try:
        ss=input()
        a,A,num,space=0,0,0,0
        for i in ss:
            if i.islower():
                a+=1
            elif i.isupper():
                A+=1
            elif i.isdigit():
                num+=1
            elif i.isspace():
                space+=1
        print(a,A,num,space)
    
    except EOFError:
        break
