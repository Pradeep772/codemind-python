n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            print(end="0")
        else:
            print(end="x")
    print("")