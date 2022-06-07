m=int(input())
n=int(input())
sum=0
b=0
for i in range(1,m):
    if(m%i==0):
        sum=sum+i
for j in range(1,n):
    if(n%j==0):
        b=b+j
if(m==b and n==sum):
    print('Amicable')
else:
    print('Not Amicable')