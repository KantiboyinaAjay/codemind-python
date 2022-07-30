a,b=map(int,input().split())
m=[]
n=[]
for i in range(a):
    u=list(map(int,input().split()))
    m.append(u)
i=0
while i!=b:
    l=0
    for j in m:
        l+=j[i]
    n.append(l)
    i+=1
print(*n)