l=[]
a=int(input("Enter  a  value"))
b=int(input("Enter  b  value"))
c=int(input("Enter  c  value"))
d=int(input("Enter  d  value"))
if a>b and  a>c and  a>d:
    l.append("A  is big")
elif b>a and b>c and b>d:
    l.append("B   is  big")
elif c>a and c>b  and c>d:
    l.append(" C is  big")
else:

    l.append("D  is  big") 
print(l)