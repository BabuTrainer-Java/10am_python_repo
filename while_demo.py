
num=int(input("Enter  number"))
rev=0
t=(0,)
l1=list(t)
while num!=0:
    n1=num % 10
    rev=rev*10+n1
    num=num // 10
l1.append(rev)

t=tuple(l1)
print("reverse ::",t)
