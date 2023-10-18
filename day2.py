'''a,b,c=10,20,30
print(a if a>b and a>c else b if b>c else c)'''
'''n=5
mat=list()
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    mat.append(a)
    
for i in range(n):
    for j in range(n):
        print(mat[i][j],end='')
    print()
dc=0
for i in range(n):
    dc+=h '''
'''n="hello,how is your family?!"[::-1]
n.split(n)

print(n)'''
"""n=int(input())
for i in range(40,101):
    i=i*i
print(i)
import math

start = 40
end = 100

print(f"Perfect square root numbers between {start} and {end}:")

for num in range(start, end + 1):
    sqrt_num = math.sqrt(num)
    int_sqrt_num = int(sqrt_num)

    if int_sqrt_num ** 2 == num:
        print(num)
"""
#start = 40
#end = 100

#print(f"Perfect square numbers between {start} and {end}:")
"""
for num in range(40,100):
    sqrt = int(num ** 0.5)
    if sqrt * sqrt == num:
        print(num)
        o/p:49
64
81
    """    
#print(chr(3077))
#print(chr(3078))
print(bin(7)[2:])
"""a=int(input())
b=int(input())
m=(bin(a)[2:])
n=(bin(b)[2:])
s=m+n
print('{0:1}'.format(s))"""