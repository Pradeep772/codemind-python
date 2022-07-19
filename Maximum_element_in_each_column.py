def fun(mat,r,c):

    for i in range(c):

        p=mat[0][i]

        for j in range(r):

            if mat[j][i]>p:

                p=mat[j][i]

        print(p)

r,c=map(int,input().split())

mat=[]

for i in range(r):

    a=[]

    a=list(map(int,input().split()))

    mat.append(a)  

#print(mat)    

fun(mat,r,c);

