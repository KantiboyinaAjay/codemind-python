from math import *
x = int(input())
for i in range(1,int(sqrt(x))+1):
    c=0
    if i*i==x:
        c=1
if c==1:
    print("True")
else:
    print("False")