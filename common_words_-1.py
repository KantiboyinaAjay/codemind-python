x = list(map(str,input().lower().split()))
y = list(map(str,input().lower().split()))
s=0
l=[]
m=[]
for i in x:
    if i in y:
        l.append(i)
for i in y:
    if i in x:
        m.append(i)
for i in l:
    if i in m:
        s+=1
print(s)