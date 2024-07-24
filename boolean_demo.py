a  =True
b  =False
print(type(a))
print(type(b))
print(True  and  True) # True 
print(True  or  False) # True
print(not True) #  False
print(bool([]))  #  false
print(bool(""))   #  false
print(bool([10,20,40]))  #  true

def  f1():
    return True

def  f2():
    return False

print(f1() and  f2())
print(f1() or  f2())
print(not f1())



