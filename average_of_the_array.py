n=int(input())
arr=list(map(int,input().strip().split()))[:n]
avg=sum(arr)/n
print("%.2f"%avg)