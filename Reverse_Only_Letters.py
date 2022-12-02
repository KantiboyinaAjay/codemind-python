n=input()
l=[]
k=""
for i in n:
    if i.isalpha():
        l.append(i)
l.reverse()
i=0
for u in n:
    if u.isalpha():
        k+=l[i]
        i+=1
    else:
        k+=u
print(k)