'''# circular linked list
class node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None
class sll:
    def __init__(self):
        self.head=None
        self.tail=None
        #self.head.prev=None
    def insert_at_start(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
            self.tail.next=self.head
            self.head.prev=self.tail
            print(self.tail.val)
    def insert_at_end(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            new=node(data)
            new.prev=self.tail
            self.tail.next=new
            self.tail=new
            self.tail.next=self.head
            self.head.prev=self.tail
            print(self.tail.val)
    def delete_at_start(self):
        if self.head==None:
            return
        self.head=self.head.next
        a=self.head.prev.val
        self.tail.next=self.head
        self.head.prev=self.tail

        return a
    
    def delete_at_end(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        #a=self.tail.next.val
        self.head.prev=self.tail
        self.tail.next=self.head

        #return a
    def display(self):
        temp=self.head.next
        print(self.head.val,end="-->")
        while(temp!=self.head):
            print(temp.val,end=" -->")
            temp=temp.next
        print()
l=[2,3,4,5,6]

obj=sll()
for i in l:
    obj.insert_at_end(i)
obj.display()
obj.delete_at_end()
obj.display()
o/p:3
4
5
6
2-->3 -->4 -->5 -->6 -->
2-->3 -->4 -->5 -->'''

'''class node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
def printing(root):
    if root==None:
        return
    print(root.val)
    printing(root.left)
    printing(root.right)
    
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
printing(root)
o/p:1
2
4
5
3'''

'''
class node:
    def __init__(self,data):
        self.val=data
        self.right=None
        self.left=None
#_______________DFS______________#
def printing(root):
    if root==None:
        return
    #print(root.val)
    printing(root.left)
    print(root.val)
    printing(root.right)
    #print(root.val)
    
root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
printing(root)


#_______________BFS_____________#

q=[]
q.append(root)
while q:
    a=q.pop(0)
    print(a.val)
    if a.left:
        q.append(a.left)
    if a.right:
        q.append(a.right)
        
o/p:1
2
4
5
3
4
2
5
1
3
1
2
3
4
5'''