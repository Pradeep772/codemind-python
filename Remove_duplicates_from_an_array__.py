n=int(input())

arr=list(map(int,input().split()))

ls=[]

for i in arr:

    if i not in ls:

        ls.append(i)

print(*ls)

