x = int(input())
l = list(map(int,input().split()))
k = int(input())
c=0
n=[]
for i in list(set(l)):
    for j in l:
        if i==j:
            c+=1
    if k==c:
        print(i,end=" ")
        n.append(i)
    c=0
if n==[]:
    print('-1')