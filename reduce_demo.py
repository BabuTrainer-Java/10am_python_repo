from functools  import reduce 
def f1(x,y):
    return x+y

def f2(x,y):
    return x-y

def f3(x,y):
    return x*y
l_list=[1,2,3,4,5]
a=reduce(f1,l_list)
s=reduce(f2,l_list)
m=reduce(f3,l_list)
print("add of \n",a)
print("sub of \n",s)
print("mul of \n",m)


