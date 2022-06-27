x,y,w,h=map(int,input().split())

print(min(w-x,h-y,x,y))


#절댓값끼리 비교하는게 더 빠르네
