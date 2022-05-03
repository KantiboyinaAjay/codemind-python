x = int(input())
b=x
s=0
while x!=0:
    v = x%10
    s = s*10+v
    x = x//10
if b==s:
    print("True")
else:
    print("False")