a,b=map(int,input().split())
c=b
while True:
    if(a%c==0 and b%c==0):
        break
    c-=1
print(c)