'''Knap sack (fractional)
W=int(input())
wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
l=list(zip(wt,pr))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
maxpr=0
for weight,profit in l:
    if weight<=W:
        maxpr+=profit
        W-=weight
    else:
        maxpr+=W*(profit/weight)
        break
print(maxpr)
o/p:
30
20 10 5 15 25
100 75 40 55 65
190.0'''


''' Triplet adding nos
l=list(map(int,input().split()))
n=int(input())
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if l[i]+l[j]+l[k]==n:
                print("found")
o/p:5 8 1 2 3
15
found'''


'''#cows
def isvalid(k,stalls,mid):
    prevcow=stalls[0]
    count=1
    for i in stalls:
        if (i-prevcow)>=mid:
            count+=1
            prevcow=i
    return True if k==count else False
def solve(n,k,stalls):
    stalls.sort()
    si=0
    li=stalls[-1]-stalls[0]
    res=0
    while si<=li:
        mid=(si+li)//2
        if isvalid(k,stalls,mid):
            res=mid
            si=mid+1
        else:
            li=mid-1
    return res
n=5
k=3
stalls=[5,8,6,3,1]
print(solve(n,k,stalls))
o/p:3'''