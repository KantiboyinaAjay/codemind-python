a,b=map(int,input().split())
m=[]
for i in range(a):
    u=list(map(int,input().split()))
    m.append(u)
print(sum(max(m)))