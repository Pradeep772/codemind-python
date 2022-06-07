n=int(input())
arr=[]
for i in  range(1,n):
    if(n%i==0):
        arr.append(i)
b=(sum(arr))
if(b==n):
    print(True)
else:
    print(False)