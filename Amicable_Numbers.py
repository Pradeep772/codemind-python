m=int(input())
n=int(input())
sum=0
ev=0
for i in range(1,m):
    if(m%i==0):
        sum=sum+i
for j in range(1,n):
    if(n%j==0):
        ev=ev+j
if(sum==n and ev==m):
    print("Amicable")
else:
    print("Not Amicable")