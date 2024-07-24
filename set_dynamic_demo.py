'''
n1=int(input(" how  many  objs  you want store"))
s1={"app1"}
for x  in range(n1):
    name=input("Enter obj")
    s1.add(name)

print(s1)

n2=input("Enter  Searching obj")
for x  in  s1:
    if x == n2:
         print("the  Given  obj  is  found")
     else:
        print("the Given  obj  is not  found")
    
'''
s5={"rao","svrao","kamal","pavan","bye"}
s6={"a","b","c","d","bye"}
#s5.difference_update(s6)
s5-=s6
print(s5)
del s5
print(s5)





    


