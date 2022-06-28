x = int(input())
if x==0:
    print(True)
a,b=1,0
for i in range(x-1):
    c = a+b
    a,b=b,c
    if x==c:
        print(True)
        break
else:
    print(False)