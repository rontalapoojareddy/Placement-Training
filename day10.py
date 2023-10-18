'''
Binary Search
def l1(l,si,li,key):
    mid=(si+li)//2
    if si>li:
        return False
    if l[mid]==key:
        return l[mid]
    if l[mid]<key:
        return l1(l,mid+1,li,key)
    return l1(l,si,mid-1,key)
l=list(map(int,input("enter elements").split()))
key=int(input("enter search"))
si=0
li=len(l)-1
print(l1(l,si,li,key))
o/p:enter elements1 2 3 4 5
enter search4
4'''


''' Binary search with if element found element else the small element than entered (FLOOR)
def bs(l,si,li,key):
    mid=(si+li)//2
    if si>li:
        return l[mid]
    if l[mid]==key:
        return l[mid]
    if l[mid]<key:
        return bs(l,mid+1,li,key)
    return bs(l,si,mid-1,key)
l=list(map(int,input("enter elements:").split()))
key=int(input("eneter search element"))
si=0
li=len(l)-1
print(bs(l,si,li,key))
o/p:
enter elements:1 2 5
eneter search element4
2
enter elements:1 5 4 
eneter search element5
5'''


'''
Binary search with if element found index element else the small element than entered index
def bs(l,si,li,key):
    mid=(si+li)//2
    if si>li:
        return [mid]
    if l[mid]==key:
        return [mid]
    if l[mid]<key:
        return bs(l,mid+1,li,key)
    return bs(l,si,mid-1,key)
l=list(map(int,input("enter elements:").split()))
key=int(input("eneter search element"))
si=0
li=len(l)-1
print(bs(l,si,li,key))
o/p:enter elements:1 2 3
eneter search element1
[0]
enter elements:2 5 9
eneter search element1
[-1]'''


'''def bsceil(l,target,si,li,ceil):
    if si<=li:
        mid=(si+li)//2
        if l[mid]==target:
            return l[mid]
        if l[mid]<target:
            floor=l[mid]
            return bsceil(l,target,mid+1,li,ceil)
        else:
            ceil=l[mid]
            return bsceil(l,target,si,mid-1,ceil)
        return ceil
l=[2,6,8,9,10]
target=8
ceil=float('inf')
si=0
li=len(l)-1
print(bsceil(l,target,si,li,ceil))
o/P:8'''


'''def bsfloor(l,target,si,li,floor):
    if si<=li:
        mid=(si+li)//2
        if l[mid]==target:
            return l[mid]
        if l[mid]<target:
            floor=l[mid]
            return bsfloor(l,target,mid+1,li,floor)
        else:
            
            return bsfloor(l,target,si,mid-1,floor)
        return floor
l=[2,6,8,9,10]
target=8
si=0
li=len(l)-1
floor=-1
print(bsfloor(l,target,si,li,floor))
o/p:8'''

'''
SQUARE ROOT NO
n=int(input())
si=0
li=n//2
floor =-1
while si<=li:
    mid=(si+li)//2
    sq=mid*mid
    if sq==n:
        floor=mid
        break
    elif sq<n:
        floor=mid
        si=mid+1
    else:
        li=mid-1
print(floor)
o/p:16
4'''

'''def bs(l, si, li, key, floor, ceil):
    if si > li:
        return floor, ceil
    
    mid = (si + li) // 2

    if l[mid] == key:
        return key, key

    if l[mid] < key:
        floor = l[mid]
        return bs(l, mid + 1, li, key, floor, ceil)
    else:
        ceil = l[mid]
        return bs(l, si, mid - 1, key, floor, ceil)

l = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter search element: "))
si = 0
li = len(l) - 1
floor = -1
ceil = float('inf')

floor, ceil = bs(l, si, li, key, floor, ceil)

print("Floor:", floor)
print("Ceil:", ceil)
o/p:Enter elements: 1 2 3 4
Enter search element: 2
Floor: 2
Ceil: 2

Enter elements: 2 4 5 1 6
Enter search element: 1
Floor: -1
Ceil: 2'''

'''
Square root using binary search algorithm
def sq(num,ep=1e-6):
    if num<0:
        raise ValueError("cannot compute square")
    if num<1:
        left,right=num,1
    else:
        left,right=0,num
    while abs(left-right)>ep:
        mid=(left+right)/2
        midsq=mid*mid
        if midsq<num:
            left=mid
        else:
            right=mid
    return(left+right)/2
num=int(input())
res=sq(num)
print(f"the square root of {num}=",res)
o/p:4
the square root of 4= 1.9999995231628418

16
the square root of 16= 3.999999523162842'''


'''#Quick sort
def qsort(l,s,e):
    pi=l[e]
    i=s-1
    for j in range(s,e):
        if l[j]<pi:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[e]=l[e],l[i+1]
    return i+1
def quick(l,s,e):
    if s<e:
        pi=qsort(l,s,e)
        quick(l,s,pi-1)  
        quick(l,pi+1,e)
l=list(map(int,input().split()))
quick(l,0,len(l)-1)
print(l)
o/p:3 2 1 8 4
[1, 2, 3, 4, 8]'''


'''
Merge Sort
def mergesort(l,inversion):
  if len(l)>1:
    mid=len(l)//2
    left=l[:mid]
    right=l[mid:]  
    li=mergesort(left,inversion)
    ri=mergesort(right,inversion)
    
    i=j=k=0
    while i<len(left) and j<len(right):
      if left[i]<right[j]:
        l[k]=left[i]
        i+=1
        k+=1
      else:
        l[k]=right[j]
        j+=1
        k+=1
        inversion+=len(left)-i
    while i<len(left):
      l[k]=left[i]
      i+=1
      k+=1
    while j<len(right):
      l[k]=right[j]
      j+=1
      k+=1
    return li+ri+inversion
  return 0
    
l=list(map(int,input().split()))
k=mergesort(l,0)
#print(k)
print(l)
o/p:1 8 6 2 4 5
[1, 2, 4, 5, 6, 8]'''
