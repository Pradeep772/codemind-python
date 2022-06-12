a=int(input())
arr=[]
for i in range(1,a):
    if(a%i==0):
        arr.append(i)
        
if sum(arr)==a:
    print(True)
else:
    print(False)