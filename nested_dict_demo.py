MObjs={
"emp1":{
   "eid":"101",
   "ename":"101",
   "esal":"19000"
 },
"emp2":{
   "eid":"102",
   "ename":"kavitha",
   "esal":"12000"
 },
"emp3":{
   "eid":"103",
   "ename":"nani",
   "esal":"14000"
 }

}
print("Before  updating")
print("emp1 esal::",MObjs["emp1"]["esal"])
print("emp2 esal::",MObjs["emp2"]["esal"])
print("emp3 esal::",MObjs["emp3"]["esal"])
MObjs["emp1"]["esal"]=40000
MObjs["emp2"]["esal"]=50000
MObjs["emp3"]["esal"]=60000
print("After  updating:::")
print("emp1 esal::",MObjs["emp1"]["esal"])
print("emp2 esal::",MObjs["emp2"]["esal"])
print("emp3 esal::",MObjs["emp3"]["esal"])
#  how  to  remove  last  obj  from   dict
MObjs
print("after  calling  pop")
del MObjs["emp1"]["esal"]
print([MObjs])
for x ,y in  MObjs.items():
    print(x,"::::",y)

MObjs.clear()
print("after  calling clear fun")
print(MObjs)