'''a=68
print(chr(a))#D'''
'''
a=input()
if(a.isupper()):
    print(ord(a)-64)
else:
    print(ord(a)-96)'''
'''a=input()
if(ord(a)>96):
    print(ord(a)-96)
else:
    print(ord(a)-64)'''
'''a=input()
b=int(input())
if(ord(a)+b>122):
    print(chr((ord(a)+b)-26))
else:
    print(chr(ord(a)+b))
o/p:h x
3     4
k      b'''
'''a=4
b=2
a=a+1
b=b-2
c=(a)^(b+1)//XOR
print(c)#4
'''
'''
for i in range(-6,-15,-2):
    print(i)
    i=i-2
o/p:-6
-8
-10
-12
-14'''
'''
a=int(input())
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
    print()
o/p:4
* 
* * 
* * * 
* * * * '''
'''
a=int(input())
for i in range(a):
    print("* "*(i+1))
o/p:5
* 
* * 
* * * 
* * * * 
* * * * *'''
'''a=int(input())
for i in range(a):
    for j in range(a-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=' ')
    print()
o/p:3
   * 
  * * 
 * * * '''
'''a=int(input())
for i in range(a):
    print(" "*(a-i)+"* "*(i+1))
o/p:
    3
   * 
  * * 
 * * * '''
'''a=int(input())
for i in range(a):
    print(" "*(i+1)+"* "*(a-i))
o/p:4
 * * * * 
  * * * 
   * * 
    * '''
'''a=int(input())
for i in range(a):
    print(" "*(a-i)+"* "*(i+1))
for i in range(a):
    print(" "*(i+1)+"* "*(a-i))
o/p:4
    * 
   * * 
  * * * 
 * * * * 
 * * * * 
  * * * 
   * * 
    * '''
'''a=int(input())
for i in range(0,a):
    print(str(i+1)*(i+1))
o/p:3
1
22
333'''
'''
a=int(input())
for i in range(1,a+1):
    print(((10**i)//9)*i)
o/p:5
1
22
333
4444
55555'''
'''def cse():
    print("Hi")
def ece():
    print("Hello")
ece()
cse()
cse()
ece()
o/p:
    Hello
Hi
Hi
Hello'''
'''def cse():
    print("Hi")
def ece(x,y):
    print("Hello",x+y)
ece(5,6)
cse()
o/p:Hello 11
Hi'''
'''def cse():
    print("Hi")
def ece(*x):
    print("Hello",x)
ece(5,6,3,)
cse()
o/p:Hello (5, 6, 3)// no error its unpacking
Hi'''
'''def cse():
    print("Hi")
def ece(x,y=10):
    print("Hello",x,y)
ece(5)
cse()
o/p:Hello 5 10
Hi'''
'''def cse():
    print("Hi")
def ece(x,y=50,z=12):
    print("Hello",x,y+z)
ece(5+3,5,8)
cse()
o/p:Hello 8 13
Hi'''
'''def cse(x):
    print("Hi")
    print(x)
def ece(x):
    print("Hello")
    cse(x+3)
    print(x)
ece(5)
cse(4)
print(2)
o/p:Hello
Hi
8
5
Hi
4
2'''
'''def cse():
    print("Hi")
    ece()
def ece():
    print("Hello")
    cse()
ece()
cse()
print(2)
o/p:
error for 994
and get 6 times output'''
'''def cse():
    return 0
    print("Hi")
    cse()//no out put
cse()'''
'''
def cse():
    
    print("Hi")
    cse()//infinite loop
    return 0
cse()'''
'''
controlling recursion
def cse(x):
    if(x==0):
        return 0
    print("Hi")
    cse(x-1)
cse(4)
o/p:Hi
Hi
Hi
Hi'''
'''  controlling recursion
def cse(x):
    if(x==0):
        return 0
    print(x)
    cse(x-1)
    print(x)
    # return 0
cse(4)
o/p:4
3
2
1
1
2
3
4'''
'''def cse(x):
    if(x==0):
        return 0
    print(x)
    print(cse(x-1))
    print(x)
cse(4)
o/p:4
3
2
1
0
1
None
2
None
3
None
4'''
'''def cse(x):
    if(x==0):
        return 0
    print(x)
    print(cse(x-1))
    print(x)
    return 0
cse(4)
o/p:4
3
2
1
0
1
0
2
0
3
0
4'''
'''def cse(x):
    if(x==0):
        return 0
    print(x)
    print(cse(x-1))
    print(x)
    return 18
cse(4)
o/p:4
3
2
1
0
1
18
2
18
3
18
4'''
'''def cse(x):
    if(x==0):
        return 0
    return x+cse(x-1)
print(cse(4))#o/p:10'''
'''def cse(x):
    if(x==0):
        return 1
    return x*cse(x-1)
print(cse(5))#o/p:120'''
'''def cse(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    return cse(x-1)+cse(x-2)
print(cse(4))#o/p:3
'''
'''def cse(x):
    if(x==1):
        return 2
    if(x==2):
        return 3
    return cse(x-1)+cse(x-2)
print(cse(4))#o/p:8
'''
'''def cse(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    return cse(x-1)+cse(x-2)
print(cse(8))#o/p:21
'''
'''def cse(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    return cse(x-1)+cse(x-2)
for i in range(1,11):
    print(cse(i),end=" ")
o/p:1 1 2 3 5 8 13 21 34 55 '''
'''class cse:
    pass
a=10
print(a)#o/p=10
'''
'''class cse:
    def qwer(self):
        print("hi")
a=cse()
print(a)
o/p:<__main__.cse object at 0x041F7D50>
'''
'''class cse:
    def qwer(self):
        print("hi")
a=cse()
a.qwer()#o/p:hi
'''
'''class cse:
    def qwer(self):
        print("hi")
a=cse()
a.qwer()
cse.qwer(a) //or cse.qwer(20) same output we get
#o/p:hi
hi'''
'''class cse:
    def qwer():
        print("hi")
a=cse()
cse.qwer()#non static method
o/p:hi'''
'''class cse:
    x=10
    def __init__(self):
        self.y=30
    def qwer(self):
        print("hi")
a=cse()
a.qwer()
print(a.x,a.y)
o/p:hi
10 30'''
'''class cse:
    x=10
    def __init__(self):
        self.y=30
    def qwer(self):
        print("hi")
a=cse()
a.qwer()
print(cse.x,a.y)// static directly can accessed,non static required an object
o/p:hi
10 30'''
'''class cse:
    x=10
    def __init__(self):
        self.y=30
    def qwer(self):
        print("hi",self.y)
a=cse()
a.qwer()
o/p:hi 30'''
'''class cse:
    x=10
    def __init__(self,k):
        self.y=k
    def qwer(self):
        print("hi",self.y)
a=cse(80)
a.qwer()
o/p:hi 80'''
'''class cse:
    x=10
    def __init__(self,k):
        self.y=k
    def qwer(self):
        print("hi",self.y)
a=cse(80)
b=cse(12)
a.qwer()
b.qwer()
o/p:hi 80
hi 12'''
'''class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self):
        self.head=None
    def creat(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)   
b=cse()
b.creat(10)
b.creat(20)
b.creat(30)
b.creat(40)
print(b.head.next.next)'''
class node:
    def __init__(self,z):
        self.data=z
        self.next=None
class cse:
    def __init__(self):
        self.head=None
    def creat(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=node(x)
    def add_front(self,x):
        if(self.head==None):
            self.head=node(x)
        else:
            temp=node(x)
            temp.next=self.head
            self.head=temp
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end='->')
            temp=temp.next
b=cse()
c=cse()
b.creat(10)
b.creat(20)
c.creat(100)
b.add_front(60)
b.creat(30)
b.creat(40)
c.creat(500)
c.add_front(50)
c.display()