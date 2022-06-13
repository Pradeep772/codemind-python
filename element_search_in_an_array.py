n=int(input())
a=list(map(int,input().strip().split()))[:n]
b=int(input())
c=0
for i in range(0,n):
    if a[i]==b:
        c+=1
if(c!=0):
    print(True)
else:
    print(False)