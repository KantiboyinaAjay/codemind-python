x , y = map(int,input().split())
l=[]
m = []
for i in range(1,y+1):
    n = i*x
    l.append(n)
for j in l:
    if j%y==0:
        print(j)
        break