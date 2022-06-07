n=int(input())
temp=n
arr=[]
while n>0:
    d=n%10
    arr.append(d)
    n=n//10
print(max(arr))