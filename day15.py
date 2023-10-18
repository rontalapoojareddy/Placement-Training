'''#sliding window algorithm
l=list(map(int,input().split()))
target=int(input())
i=0
j=0
currsum=l[0]
while j<len(l):
    if currsum==target:
        print(i,j,currsum)
        break
    elif currsum>target:
        currsum-=l[i]
        i+=1
    else:
        j+=1
        currsum+=l[j]

o/p:2 5 6 7 8 10
13
0 2 13'''

'''def sieve(num):
    prime=[True]*(num+1)
    p=2
    while(p*p<=num):
        if prime[p]:
            for i in range(p*p,num+1,p):
                prime[i]=False
        p+=1
    for p in range(2,num+1):
        if prime[p]:
            print(p)
num=12
sieve(num)
o/p:2
3
5
7'''

'''a=[2,3,0,4,6,3,2,1]
for i in a:
    print("*"*i)
o/p:**
***

****
******
***
**
*'''

'''l=[2,3,0,4,6,3,2,1]
maxle=max(l)
for i in range(max(l),0,-1):
    print(f"{i:2d} | ",end="")
    for j in l:
        if j>=i:
            print(" x ",end="")
        else:
            print("   ",end="")
    print()'''