n=int(input())
c=0 
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        c+=1
if c==2:
    print('not a prime')
else:
    print('prime')