s1={"apple"}
c=0
for x  in  range(10):
    print("1.adding Element")
    print("2.Delete given Element")
    print("3.displayElements")
    print("4.update the Given Element")
    print("5.unknown op")
    print("6.search the Given Element")
    n1=input("Enter  your  choice")
    match n1:
        case "1":
            ele=input("Enter  Ele ")
            s1.add(ele)
        case "2":
            ele2=input("Enter   Ele  for  delete")
            s1.remove(ele2)
        case "3":
            for  i in s1:
                print(i)
        case "4":
            l1=list(s1)
            n1=int(input("Enter a index  for  updating ele  "))
            upele=input("Enter  a  update Ele")
            l1[n1]=upele
            s1=set(l1)
        case "5":
            exit(0)
        case "6":
             s4=input("Enter  a  Searching Ele")
             for  x1 in s1:
                if x1==s4:
                    c=c+1
                else:
                    c=0
                if  c==1:
                    print("Ele is  Found")
                 