l1=[50,30,10,20,5]
l2=[70,34]
l1.extend(l2)
print("after  adding :::",l1)
l1.pop()
print("after   calling pop:::",l1)
l1.remove(50)
print("after   calling  remove:::",l1)
l1.sort()
print("after   calling  sort  accseniding:::",l1)
l1.sort(reverse=True)
print("after   calling  sort  decseniding:::",l1)
l1.insert(2,100)
print("after   calling  insert:::",l1)
for i  in  l1:
    print(i)




