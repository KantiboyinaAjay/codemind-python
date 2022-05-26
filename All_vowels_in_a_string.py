x =(input())
c=[]
d=[]
for i in x:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c.append(i)
    elif i=='A' or i=='E' or i=='O' or i=='I' or i=='U':
        d.append(i)
n = len(set(c))
m= len(set(d))
if n==5:
    print(True)
elif m==5:
    print(True)
else:
    print(False)