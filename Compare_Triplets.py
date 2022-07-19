arr=list(map(int,input().split()))

arr2=list(map(int,input().split()))

s=0

p=0

for i in range(3):

    if(arr[i]>arr2[i]):

        s+=1

    elif(arr[i]<arr2[i]):

        p+=1

print(s,end=" ")

print(p)



