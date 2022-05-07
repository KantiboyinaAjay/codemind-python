x = int(input())
p,m=0,0
for i in range(x):
    a , b = map(int,input().split())
    for j in range(a,b+1):
        v = j%10
        if v == 2 or v==3 or v==9:
            p+=1
    print(p)
    p=0