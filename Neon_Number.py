a=int(input())
sum=0
sqt=a*a
while(sqt!=0):
    d=sqt%10
    sum=sum+d
    sqt=sqt//10

if(sum==a):
    print('Neon Number')
else:
    print('Not Neon Number')