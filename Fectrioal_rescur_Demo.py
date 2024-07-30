
def  factrioal(n):
    if n==0:
        return  1
    else:
        return  n*factrioal(n-1)
 x1=int(input("Enter  number"))
 print("factorial Number::",factrioal(x1))       