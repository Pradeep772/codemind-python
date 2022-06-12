a=int(input())
b=a*a
sum=0
while(b>0):
    d=b%10
    sum=sum+d
    b=b//10
if(sum==a):
    print("Neon Number")
else:
    print("Not Neon Number")