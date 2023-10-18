'''#Magic Square
n=int(input())
sq=[[0]*n for i in range(n)]
num=1
i=n//2
j=n-1
while num<=(n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if sq[i][j]:
        i=i+1
        j=j-2
        continue
    sq[i][j]=num
    num+=1
    i=i-1
    j=j+1
#print(sq)#5
#[[9, 3, 22, 16, 15], [2, 21, 20, 14, 8], [25, 19, 13, 7, 1], [18, 12, 6, 5, 24], [11, 10, 4, 23, 17]]
for i in sq:
    print(*i)#* indicates no brackets [] in output# print(*i,sep=', ')
print("magic constant:",n*((n*n)+1)//2)
o/p:3
2 7 6
9 5 1
4 3 8
magic constant: 15'''
'''# magic square using
recursion
def generate(n):
    sq=[[0]*n for i in range(n)]
    def fill(i,j,num):
        if num>(n*n):
            return sq
        if i<0 and j==n:
            i=0
            j=n-2
        else:
            if i<0:
                i=n-1
            if j==n:
                j=0
        if sq[i][j]:
            i=i+1
            j=j-2
            return fill(i,j,num)
        sq[i][j]=num
        return fill(i-1,j+1,num+1)
    return fill(n//2,n-1,1)
n=int(input())
print(generate(n))
print("magic constant:",n*((n*n)+1)//2)'''
'''
#bubblle sort
n=int(input())
l=list(map(int,input().split()))
for i in range(1,n):
    for j in range(n-i):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
o/p:5
9 7 5 1 2
[1, 2, 5, 7, 9]'''
'''#selection sort
n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    mini=i
    for j in range(i+1,n):
        if l[j]<l[mini]:
            mini=j
    l[i],l[mini]=l[mini],l[i]
print(l)
o/p:3
4 1 8
[1, 4, 8]'''
'''# insertion
n=int(input())
l=list(map(int,input().split()))
for i in range(1,n):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
print(l)
o/p:5
7 4 1 2 9
[1, 2, 4, 7, 9]'''