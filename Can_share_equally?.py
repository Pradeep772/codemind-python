x,y=map(int,input().split())
tal=(1*x)+(2*y)
if(x==0 and y%2==0):
    print("YES")
elif(x==0 and y%2!=0):
    print("NO")
elif(tal%2==0):
    print("YES")
else:
    print("NO")