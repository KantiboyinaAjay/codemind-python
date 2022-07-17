x=int(input())
y=input()
s=0
for i in y:
    if i=='1' or i=='0':
        s+=1
if x==s:
    print(True)
else:
    print(False)