'''class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
o1=node(1)
o2=node(2)
o3=node(3)
o1.next=o2
o2.next=o3
print(o1,o1.val,o1.next)
print(o2,o2.val,o2.next)
print(o3,o3.val,o3.next)
print(o1.val,o1.next.val,o1.next.next.val)
o/p:<__main__.node object at 0x034D7B90> 1 <__main__.node object at 0x034D7BB0>
<__main__.node object at 0x034D7BB0> 2 <__main__.node object at 0x034D7BD0>
<__main__.node object at 0x034D7BD0> 3 None
1 2 3'''

'''# insert at begin
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val)
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertatbeg(i)
o.printing()
o/p:9
8
6
4
2'''

'''#insert at end
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            new=node(data)
            curr.next=new
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end='->')
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertatend(i)
o.printing()
o/p:2->4->6->8->9->'''

'''class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            new=node(data)
            curr.next=new
    def deleteatbegin(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.val
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end='->')
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.deleteatbegin()
o.printing()
'''

'''
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            curr=self.head
            while(curr.next):
                curr=curr.next
            new=node(data)
            curr.next=new
    def deleteatbegin(self):
        if self.head==None:
            return
        temp=self.head
        self.head=self.head.next
        temp.next=None
        return temp.val
    def deleteatend(self):
        if self.head==None:
            return
        temp=self.head
        while(temp.next.next):
            temp=temp.next
        temp.next=None
    def printing(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end='->')
            temp=temp.next
l=[2,4,6,8,9]
o=sll()
for i in l:
    o.insertatend(i)
o.printing()
print()
print(o.deleteatbegin())
o.printing()
print(o.deleteatend())
o.printing()
o/p:2->4->6->8->9->
2
4->6->8->9->None
4->6->8->'''


'''s='0110'
print(int(s,2))
o/p:6'''


class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
    def deleteatbegin(self):
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
    def deleteatend(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=None
    def reverse(self):
        curr=self.head
        while curr:
            curr.prev,curr.next=curr.next,curr.prev
            curr=curr.prev
        self.head,self.tail=self.tail,self.head
    def printing(self):
        temp=self.head
        while(temp):
            print(temp.val,end='->')
            temp=temp.next
l=[2,4,6,8,9]
o=dll()
for i in l:
    o.insertatend(i)
o.printing()
print()
print(o.deleteatbegin())
o.printing()
print(o.deleteatend())
o.printing()
print(o.reverse())
o.printing()
