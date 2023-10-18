"""class siva:
    def exsiva(bbroy,a):
        print("hi",a)
    def mr(bbroy,b,c):
        print("am in way",b,c)
child=siva()
child.exsiva(100)
child.mr(250,"tc")
o/p:
hi 100
am in way 250 tc
"""
""" INHERITANCE
class siva:
    def gold(wrgl):
        print("price 5L")
    def car(wgl):
        print("price 3L")
class baby1(siva):
    def bank(wgl):
        print("deposited 2l")
class baby2(siva):
    def jewels (wgl):
        print("price 10l")
b1=baby1()
b1.bank()
b1.gold()
b1.car()

b2=baby2()
#b2.bank()
b2.jewels()
b2.gold()
b2.car()
o/p:
deposited 2l
price 5L
price 3L
price 10l
price 5L
price 3L """
"""
class siva:
    def __bank__(india):#method
        print("Test 1")
    def jeno(manglore):
        print("test 2")
    def jeff(bangalore):
        print("test 3")
s=siva()
s.jeno()
s.jeff()
s.__bank__()
o/p:
test 2
test 3
Test 1
"""
"""
ONE CONSTRUCTOR
class siva:
    def __init__(mango):#method
        print("mango const")
    def __bank__(india):#method
        print("Test 1")
    def jeno(manglore):
        print("test 2")
    def jeff(bangalore):
        print("test 3")
s=siva()
s.jeno()
s.jeff()
s.__bank__()
o/p:
mango const
test 2
test 3
Test 1"""
"""MORE THAN 1 CONSTRUCTOR
class siva:
    def __init__(mango):#method
        print("default const")
    def __init__(mango1,mango2):#method
        print("2 parm const",mango2)
    def __bank__(india):#method
        print("Test 1")
    def jeno(manglore):
        print("test 2")
    def jeff(bangalore):
        print("test 3")
s=siva(200)
s.jeno()
s.jeff()
s.__bank__()
o/p:
2 parm const 200
test 2
test 3
Test 1(default const should also print so what change can be done)
"""
class siva:
    def __init__(mango):#method
        print("default const")
    def __init__(mango1,mango2):#method
       # super().mango1.__init__(mango)
        print("2 parm const",mango2)
    def __bank__(india):#method
        print("Test 1")
    def jeno(manglore):
        print("test 2")
    def jeff(bangalore):
        print("test 3")
s=siva(200)
s.jeno()
s.jeff()
s.__bank__()
n=input[][::-1]
if num > 1:

    for i in range(2, int(num/2)+1):
        
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")