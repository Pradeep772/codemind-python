def happy(n):
    temp=n
    s=0
    while n>0:
        d=n%10
        s=s+(d**2)
        n=n//10
    return s
n=int(input())
t=happy(n)
m=happy(t)
h=happy(m)
j=happy(h)
if(j==1):
    print(True)
else:
    print(False)