import math
x,y,z=map(int,input().split())
ans=math.pow(x,y)
d=ans%z
print(int(d))