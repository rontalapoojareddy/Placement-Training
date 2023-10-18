'''import random
a=input("How idiot are you?- ")
print(random.randint(1,100),'%')'''
'''n=int(input())
# 2 usages
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)
fun(n)
o/p:5
1
2
3
4
5'''
'''n=int(input())
# 2 usages
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
fun(n)
o/p:
    6
6
5
4
3
2
1'''
#palindrome time complexity O(n)
'''n=input()
a=n[::-1]
if a==n:
    print("true")
else:
    print("false")
o/p:abbba
true

abbac
false

aaa
true'''
'''#palindrome time complexity O(n/2)
s=input()
i=0
j=len(s)-1
while(i<=j):
    if s[i]!=s[j]:
        print("false")
        break
    i+=1
    j-=1
else:
    print("true")
o/p:254
false

414
true'''
''' palindrome using recursion
s=input()
def fun(s,i,j):
    if i>j:
        return True
    if (s[i]!=s[j]):
        return False
    return fun(s,i+1,j-1)
print(fun(s,0,len(s)-1))
o/p:
252
True
254
False'''
'''import turtle
s=turtle.Turtle()
s.forward(100)
s.right(90)
s.forward(100)
s.clear()
s.reset()
for i in range(4):
    s.forward(100)
    s.right(90)
    
s.clear()
s.reset()
turtle.bgcolor("black")
s.color("white")
s.circle(100)
s.clear()
s.reset()'''
''' gaming(just timepass)
import turtle
s=turtle.Turtle()
turtle.bgcolor("black")
s.color("white")
for i in range(10):
    s.circle(100)
    s.right(36)
s.clear()
s.speed(0)
for i in range(10):
    s.circle(100)
    s.circle(105)
    s.circle(110)
    s.circle(115)
    s.circle(120)
    s.right(36)
s.clear()
for i in range(300):
    s.circle(i)
    s.right(2)
s.clear()
for i in range(300):
    for j in range(4):
        s.forward(i)
        s.right(90)
    s.right(5)'''
"""
0->water,1->land find no of islands
l=[[0,1,0,1],[1,1,0,0],[0,0,1,0],[0,0,1,1]]
n=len(l)
'''l=[]
n=int(input())
for i in range(n):
    l.append(list(map(int,input().split())))'''
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
    if i<n-1:
        fun(l,i+1,j,n)
    if i>0:
        fun(l,i-1,j,n)
    if j<n-1: 
        fun(l,i,j+1,n)
    if j>0:
        fun(l,i,j-1,n)
count=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count+=1
            fun(l,i,j,n)
print(count)#3"""
'''#1->Tree 0->land no of unburnt trees (input row,col) fire starts
l=[[1,0,0,1],[1,0,0,0],[1,0,1,0],[0,1,1,1]]
n=len(l)'''