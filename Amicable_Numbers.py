x = eval(input())
y = eval(input())
s = 0
n = 0
for i in range(1,x):
    if x%i==0:
        s+=i
for i in range(1,y):
    if y%i==0:
        n+=i
if s==y or n==x:
    print("Amicable")
else:
    print("Not Amicable")