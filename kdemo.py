import numpy as np  
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_across_columns = np.sum(arr, axis=0)

sum_across_columns1 = np.min(arr,axis=1)

print(sum_across_columns1)



"""
a= np.arange(6).reshape((2,3))  
print(a)
b=np.transpose(a)  
print(b)  
"""