x = int(input())
l = list(map(int,input().split()))
k=0
c=0
for i in list(set(l)):
    for j in l:
        if i==j:
            c+=1
    if c==i:
        k+=1
    c=0
print(k)