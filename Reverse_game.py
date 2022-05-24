def palin(i):
    s = str(i)
    m = int(s[::-1])
    return m
x = int(input())
l = list(map(int,input().split()))
for i in l:
    n = palin(i)
    print(n,end=" ")