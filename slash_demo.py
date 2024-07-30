def   f1(a,b,/):
    print(a,"::::",b)
f1(10,20) #  valid
def   f2(a,b,/,c,d):
    print(a,"::::",b,"::",c,":::",d)
f2(10,20,30,40) #  valid
f2(10,20,c=30,d=40) #  valid

def   f3(*args):
    print(args)
f3(10,20)
f3(10)
f3()
f3(10,20,40,50,50)
def f4(a,b,/,*,c,d):
    print(a,":::",b"::",c,"::::",d)
f4(10,20,c=45,d=47)


def f5(**args):
    print(args)

f5(eid=101,ename="hello",esal=19000)

def f6(*a,**args):
    print(a,":::::",args)

f6(10,20,45,57,eid=102,ename="kiran",esal=21000)


