a=int(input())
sum=0
pro=1
while(a>0):
    d=a%10
    sum=sum+d
    pro=pro*d
    a=a//10
if(sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")
