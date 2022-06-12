import math
n=int(input())
b=int(n**2)
num_of_digit=len(str(n))
d=b%pow(10,num_of_digit)


if(d==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")