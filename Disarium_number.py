x = eval(input())
b=x
n = len(str(x))
s=0
while x!=0:
    v = x%10
    x=x//10
    m = v**n
    s+=m
    n-=1
if s==b:
    print("True")
else:
    print("False")