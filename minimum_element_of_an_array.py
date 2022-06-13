n=int(input())
a=list(map(int,input().strip().split()))[:n]
a.sort()
print(*a[:1])