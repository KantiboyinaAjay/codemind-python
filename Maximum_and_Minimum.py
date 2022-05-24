x = int(input())
l = list(map(int,input().split()))
k=[]
n=1
c=0
for i in l:
    for j in l:
        if i==j:
            c+=1
    if c==i:
        k.append(i)
        n=0
    c=0
if k==[]:
    print('-1')
else:
    print(min(k),end=" ")
    print(max(k))