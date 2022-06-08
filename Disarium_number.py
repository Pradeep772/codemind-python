n=int(input())
le=len(str(n))
temp=n
s=0
while n>0:
    d=n%10
    s=s+int(d**le)
    n=n//10
    le-=1
if(s==temp):
    print(True)
else:
    print(False)