emp={
"eid":"101",
"ename":"kamal",
"esal":"19000",
"age":"35"
}
dept={
"did":"101",
"dname":"cse",
"dlocation":"hyd"    
}
print(emp["ename"],"::::",dept["dname"])
print("keys::::")
for x in emp.keys():
    print(x)
print(" values::::")    
for v in emp.values():
    print(v)    

print("Iterating Keys and values")
for k,y in  emp.items():
    print(k,"::::",y)