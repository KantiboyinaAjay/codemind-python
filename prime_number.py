y = eval(input())
x = 1
flag=0
while(x<=y):
    if(y%x==0):
        flag+=1
    x+=1
if(flag==2):
    print("prime")
else:
    print("not a prime")