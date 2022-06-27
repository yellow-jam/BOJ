
#숫자 몇번에 해당하는지 알려주는 함수
def num(c):
    if 'A'<=c<='C':
        return 2
    elif 'D'<=c<='F':
        return 3
    elif 'G'<=c<='I':
        return 4
    elif 'J'<=c<='L':
        return 5
    elif 'M'<=c<='O':
        return 6
    elif 'P'<=c<='S':
        return 7
    elif 'T'<=c<='V':
        return 8
    elif 'W'<=c<='Z':
        return 9
    
ss=input()
time=0
for char in ss:
    time+=num(char)+1
print(time)


# abc7848 님의 방법 (제출번호 31716163)
'''
alphabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
'''
#흠... 쉽지않은디

'''
#sol_2

alphabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
sec = 0

for unit in alphabet_list:
    for i in unit:
        for x in word:
            if i == x:
                sec += alphabet_list.index(unit) + 3
                
print(sec)
'''
