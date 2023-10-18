'''# Quick sort
def qsorting(l,start,end):
    pi=l[end]
    i=start-1
    for j in range(start,end):
        if l[j]<pi:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1
def quick (l,start,end):
    if start<end:
        pi=qsorting(l,start,end)
        quick(l,start,pi-1)
        quick(l,pi+1,end)
l=list(map(int,input().split()))
quick(l,0,len(l)-1)
print(l)
o/p:
9 8 7 
[7, 8, 9]'''
'''
Inverse Count
l=list(map(int,input().split()))
count=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            count+=1
print("count =",count)
o/p:3 2 1 4 5
count = 3'''
'''#Merge Sort
def mergesort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        mergesort(left)
        mergesort(right)
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
            while i<len(left):
                l[k]=left[i]
                i+=1
                k+=1
            while j<len(right):
                l[k]=right[j]
                j+=1
                k+=1
l=list(map(int,input().split()))
mergesort(l)
print(l)'''

'''
subset
def isSubsetSum(set, n, sum) : 
	
	if (sum == 0) : 
		return True
	if (n == 0 and sum != 0) : 
		return False

	
	if (set[n - 1] > sum) : 
		return isSubsetSum(set, n - 1, sum); 
	return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1]) 
set = [3, 34, 4, 12, 5, 2] 
sum = 12
n = len(set) 
if (isSubsetSum(set, n, sum) == True) : 
	print("Found a subset with given sum") 
else : 
	print("No subset with given sum") 
	'''
'''Merge and inversion count
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
print('count=',k)
print(l)
o/p:3 2 1
count= 3
[1, 2, 3]
 '''
''' all possible subsets equal to sum
def find_subsets(nums,target):
    def backtrack(start,curr_sum,subset):
        if curr_sum == target:
            res.append(subset[:])
            return
        if curr_sum>target or start==len(nums):
            return
        subset.append(nums[start])
        backtrack(start+1,curr_sum+nums[start],subset)
        subset.pop()
        backtrack(start+1,curr_sum,subset)
    res=[]
    backtrack(0,0,[])
    return res
nums=list(map(int,input().split()))
target_sum=int(input())
result=find_subsets(nums,target_sum)
if result:
    print(result)
else:
    print("no subset with sum")
    o/p:
    1 2 3 4 5
9
[[1, 3, 5], [2, 3, 4], [4, 5]]
    '''