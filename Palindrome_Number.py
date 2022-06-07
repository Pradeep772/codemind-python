n=int(input())
for i in range(n):
    t=int(input())
    rev=0
    temp=t
    while(t>0):
        d=t%10
        rev=(rev*10)+d
        t=t//10
    t=temp
    if t==rev:
        print(True)
    else:
        print(False)
        