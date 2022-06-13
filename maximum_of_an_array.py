n=int(input())
a=list(map(int,input().strip().split()))[:n]
a.sort()
a.reverse()
print(*a[:1])