x = list(map(str,input().split()))
y = list(map(str,input().split()))
c=0
d=[]
e=[]
for i in x:
   d.append(i.lower())
for j in y:
    e.append(j.lower())
for k in d:
    if e.count(k)!=0:
        c+=1
print(c)