'''
data = [(1, 'banana'), (2, 'apple'), (3, 'cherry')]

# Sort by the second element of each tuple (the fruit name)
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(2, 'apple'), (1, 'banana'), (3, 'cherry')]

number_=[lambda x=x:x**2 for x  in range(0,10)]
for  n in number_:
    print(n())
'''
my_List = [[3, 5, 8, 6]]      
sort_List =my_List.sort()     
print(sort_List) 
m=list(map(filter(lambda  x:x<35,my_List)))
print(m)
