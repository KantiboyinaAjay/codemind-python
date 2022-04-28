x = eval(input())
n=x
s=0
while x!=0:
    v = x%10
    x=x//10
    s+=v
if n%s==0:
    print("True")
else:
    print("False")