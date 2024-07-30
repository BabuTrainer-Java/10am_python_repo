def emp(eid,ename,esal):
    l=[]
    l.append(eid)
    l.append(ename)
    l.append(esal)
    for  x in l:
         print(x)
id=int(input("Enter Eid"))
name=input("Enter  Ename")
sal=int(input("Enter  a Esal"))    
emp(id,name,sal)