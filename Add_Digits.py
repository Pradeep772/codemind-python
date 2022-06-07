def add(n):
    temp=n
    s=0
    while n:
        d=n%10
        s=s+d
        n=n//10
    return s
n=int(input())
t=add(n)
m=add(t)
f=add(m)
print(f)