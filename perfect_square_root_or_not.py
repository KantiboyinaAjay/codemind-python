x = int(input())
n = int(x**0.5)
c=0
for i in range(1,n+1):
    if i*i==x:
        print(True)
        c=1
if c==0:
    print(False)