n=int(input())
v=0
if(n<0):
    n=-n
    v=+1
rev=0
while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10
if v==0:
    print(rev)
if v==1:
    print(-(rev))