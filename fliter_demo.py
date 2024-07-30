numbers_=[1,2,3,4,5,6]
even_List=list(filter(lambda num:num%2==0,numbers_))
odd_list=list(filter(lambda num:num%2!=0,numbers_))
print("Even List \n",even_List)
print("odd List \n",odd_list)
d1=[37,34,34]
c=0
stu_status=list(filter(lambda s:s<35, d1))
if  stu_status==True:
    
    stu_status="Pass"
else:
    c=c+1
    stu_status="fail"
print(stu_status,"\n",c)
