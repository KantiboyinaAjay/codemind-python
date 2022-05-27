x = int(input())
l = list(map(int,input().split()))
c=1
for i in l:
    for j in l:
        if i!=j:
            c*=j
    print(c,end=" ")
    c=1