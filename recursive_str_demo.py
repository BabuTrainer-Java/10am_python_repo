def f1(s):
    if len(s)==0:
        return  s
    else:
         return s[-1] + f1(s[:-1])
s1=input("Enter a String ")
s2=input("Enter a String ")
s3=input("Enter a String ")
s4=s1 +  s2 + s3
print("reverse ::\n",f1(s4))


