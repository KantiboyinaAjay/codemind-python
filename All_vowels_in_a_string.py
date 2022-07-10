x = input()
m=[]
l=[]
for i in x:
    if i=='a':
        l.append('a')
    elif i=='e':
        l.append('e')
    elif i=='i':
        l.append('i')
    elif i=='o':
        l.append('o')
    elif i=='u':
        l.append('u')
    elif i=='A':
        m.append('A')
    elif i=='E':
        m.append('E')
    elif i=='I':
        m.append('I')
    elif i=='O':
        m.append('O')
    elif i=='U':
        m.append('U')
l = set(l)
m = set(m)
if len(l)==5:
    print(True)
elif len(m)==5:
    print(True)
else:
    print(False)