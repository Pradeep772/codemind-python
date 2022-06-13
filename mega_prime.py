def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n=int(input())
if(prime(n)):
    v=0
    c=0
    while n!=0:
        d=n%10
        if(prime(d)):
            v+=1
        n=n//10
        c+=1
    if v==c:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")