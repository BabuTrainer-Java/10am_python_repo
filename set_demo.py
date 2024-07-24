set1={"app1","app2","suma","suma","hello","bye"}
print(set1)
set2={True,False,10,20.5,1,0}
l1=[1,1,2,2,3,3,4,4]
set3=set(l1)
t1=(5,6,7,8,8,9)
set4=set(t1)
s5=set1.union(set2,set3,set4)
print(s5)
s6=set1 | set2 |  set3 | set4
for  x in  s6:
    print(x)


