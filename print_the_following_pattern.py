n=int(input())
for i in range(n,0,-1):
    m=64+i
    for j in range(i):
        print(chr(m),end=" ")
    print()