x , y = map(int,input().split())
c=0
for i in range(x):
    l = list(map(int,input().split()))
    n = sorted(l)
    m = sorted(l,reverse=True)
    if l==n:
        c+=1
    elif l==m:
        c+=1
print(c)