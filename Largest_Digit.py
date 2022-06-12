n=int(input())
l=[]
m=0
while(n>0):
    d=n%10
    l.append(d)
    n=n//10
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
print(m)        