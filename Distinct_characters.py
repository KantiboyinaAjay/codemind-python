z = input().lower()
for i in sorted(z):
    if i>='a' and i<='z':
        if z.count(i)==1:
            print(i,end="")