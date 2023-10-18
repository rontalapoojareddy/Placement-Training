'''l=[2,4,8,3,8,1,2,4,7,4]
count=[0 for i in range(10)]
for i in range(len(l)):
    count[l[i]]+=1
for i in range(1,len(count)):
    count[i]+=count[i-1]
res=[0]*len(l)
for i in range(len(l)):
    res[count[l[i]]-1]=l[i]
    count[l[i]]-=1
print(res)
o/p:[1, 2, 2, 3, 4, 4, 4, 7, 8, 8]'''
'''

l=[]
while 1:
    s=input()
    if s=='':
        break
    a=list(map(int,s.split(",")))
    l.append(a)
for i in l:
    print(", ".join(map(str,i)))
o/p:
    2,5,4

2, 5, 4'''


'''for i in range(10):
    print("hhhhhh",i,"ndsjnsdjwh")
o/p:
    hhhhhh 0 ndsjnsdjwh
hhhhhh 1 ndsjnsdjwh
hhhhhh 2 ndsjnsdjwh
hhhhhh 3 ndsjnsdjwh
hhhhhh 4 ndsjnsdjwh
hhhhhh 5 ndsjnsdjwh
hhhhhh 6 ndsjnsdjwh
hhhhhh 7 ndsjnsdjwh
hhhhhh 8 ndsjnsdjwh
hhhhhh 9 ndsjnsdjwh'''


'''for i in range(5):
    print("* "*i)
o/p:
* 
* * 
* * * 
* * * *'''


'''a=range(1,10,2)
print(a,type(a))
o/p:range(1, 10, 2) <class 'range'>'''


'''def fun(a):
    return a*a
l=[2,3,4,5]
l=list(map(fun,l))
print(l)
o/p:[4, 9, 16, 25]'''


'''def fun(a):
    return sum(a)
l=[[1,2,3],[5,6,7],[9,0,0]]
l=list (map(fun,l))
print(l)
o/p:[6, 18, 9]'''


'''l=[[1,2,3],[5,6,7],[9,0,0]]
l=list(map(lambda a:sorted(a),l))
print(l)
o/p:[[1, 2, 3], [5, 6, 7], [0, 0, 9]]'''


'''l=[[1,2,3],[5,6,7],[9,0,0]]
a=[2,3,4,5,6]
l=list(filter(lambda a:a%2==0,a))
print(l)
o/p:[2, 4, 6]'''


'''l=[[1,2,3],[5,6,7],[9,0,0]]
a=[2,3,4,5,6]
l=list(filter(lambda l:sum(l)<=9,l))
print(l)
o/p:[[1, 2, 3], [9, 0, 0]]'''


'''l=[[1,2,3],[5,6,7],[9,0,0]]
l.sort(key=sum)
print(l)
o/p:[[1, 2, 3], [9, 0, 0], [5, 6, 7]]'''


'''l=[[1,2,3],[5,6,7],[9,0,0]]
l.sort(key=lambda x:x[0]+x[1])
print(l)
o/p:[[1, 2, 3], [9, 0, 0], [5, 6, 7]]'''


'''l=[[1,3,2],[8,6,7],[9,0,0]]
print(max(l,key=lambda x:x[0]+x[1]))
print(l)
o/p:[8, 6, 7]
[[1, 3, 2], [8, 6, 7], [9, 0, 0]]'''


'''ZIP FUNCTION
a=[1,2,3,4,5]
b=[5,9,8,7,6]
print(list(zip(a,b)))
O/P:[(1, 5), (2, 9), (3, 8), (4, 7), (5, 6)]'''


'''a=[1,2,3,4,5]
b=[5,9,8,7,6]
print(list(enumerate(a)))
o/p:[(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]'''


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


''' Sum of array elements
a = list(map(int,input().split()))
sum= 0
for num in a:
    sum += num
print("The sum is:", sum)
o/p:1 2 3
The sum of array elements is: 6'''


'''
Sum of array elements(using divide and conqure)
def sum(l,si,li):
    if si==li:
        return l[si]
    if si>li:
        return -1
    mid=(si+li)//2
    return sum(l,si,mid)+sum(l,mid+1,li)
l=list(map(int,input("enter numbers").split()))
print("sum =",sum(l,0,len(l)-1))
o/p:enter numbers1 2 3 4 
sum = 10'''


''' MAX Element in an array
a = list(map(int,input("enter numbers").split()))
element = max(a)
print("The maximum in array:",element)
o/p:enter numbers1 2 3 7 5 4
The maximum in array: 7'''
''' MAX Element in an array
a = list(map(int,input("enter numbers").split()))
max1 = a[0]
for num in a:
    if num > max1:
        max1 = num
print("The max in array = ", max1)
o/p:enter numbers1 4 5 7 2 0
The max in array =  7'''


'''
MAX Element in an array(using divide and conqure)
def sum(l,si,li):
    if si==li:
        return l[si]
    if si>li:
        return -1
    mid=(si+li)//2
    return max(sum(l,si,mid),sum(l,mid+1,li))
l=list(map(int,input("enter numbers").split()))
print("max =",sum(l,0,len(l)-1))
o/p:enter numbers4 5 6 2 1 8
max = 8'''