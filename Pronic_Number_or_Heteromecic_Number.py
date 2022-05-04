x = eval(input())
c=0
for i in range(x):
    if i * (i+1) == x:
        c+=1
        break
if c==1:
    print('YES')
else:
    print("NO")