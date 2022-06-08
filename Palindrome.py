n=int(input())
rev=0
temp=n
while(n!=0):
    d=n%10
    rev=(rev*10)+d
    n=n//10
n=temp
if rev==n:
    print(True)
else:
    print(False)