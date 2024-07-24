l1=[10,1,5,10,40,7,50]
l2=[95 if x==10 else x for  x in l1]
print(l2)
l3=["even" if x%2==0 else x for  x in l1]
print(l3)
l4=["odd" if x%2!=0 else  x  for  x in l1]
print(l4)
l5=["odd" if x%2!=0 else  "even"  for  x in l1]
print(l5)
