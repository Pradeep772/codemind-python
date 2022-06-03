def palin(i):
    temp=i
    s=0
    while i:
        d=i%10
        s=s*10+d
        i=i//10
    return(s==temp)
    
n=int(input())
m=int(input())
for i in range(n,m+1):
    if palin(i):
        print(i,end=' ')