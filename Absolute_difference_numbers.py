n,k=map(int,input().split())

rev=0

t=n

while n:

    d=n%10

    rev=rev*10+d

    n=n//10

a=t%(10**k)

b=rev%(10**k)

r=0

while b:

    d=b%10

    r=r*10+d

    b=b//10

print(abs(a-r))