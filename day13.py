'''class cse:
    def fun1(self):
        print("fun1")
    def fun2(s):
        print("fun2")
class two(cse):
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
class three(two):
    def fun5(self):
        print("fun5")
o=cse()
o.fun1()
a=two()
b=three()'''
'''class cse:
    def fun1(self):
        print("fun1")
    def fun2(s):
        print("fun2")
class two(cse):
    def fun1(self):
        print("fun3")
    def fun3(self):
        print("fun4")
class three(two):
    def fun5(self):
        print("fun5")
o=cse()
o.fun1()
a=two()
a.fun1()
b=three()
o/p:fun1
fun3'''

s ="babad"
lis=[]
st=""
''''for i in range(len(s)):
    j=len(s)-1
    while i<j:
        if s[i]==s[j]:
            st=s[i:j+1]
            if st==st[::-1]:
                lis.append(st)
        st=""
        j-=1
if len(s)==1:
    print(s)
elif not lis:
    print(s[0])
else:
    print(lis[0])
o/p:bab'''

