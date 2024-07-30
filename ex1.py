categorize_age = lambda x,y,z:'x is big'  if x > y  else ('x is big' if x < z else(" x is not "))
print(categorize_age(10,19,19))
