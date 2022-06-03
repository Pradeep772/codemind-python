import math
l1=input()
l=list(map(int,l1.split()))
p=l[0]
r=l[1]
t=l[2]
ci=p*math.pow((1+r/100),t)
print("%.2f"%float(ci))