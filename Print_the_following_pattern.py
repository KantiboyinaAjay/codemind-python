n=int(input())
m=1
k=1
for i in range(n,0,-1):
    m+=1
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()
    k=m