
#Map applies a function to all the items in an input_list.
def squared(x):
	return x**2
def check(x):
	return x>3
items = [1,2,3,4,5]
x = list(map(squared, items)) # list(map(lambda x: x**2, items)) 
print(x)

#filter creates a list of elements for which a function returns true.
y = list(filter(check, items))#list(filter(lambda x: x>3, items))
print(y)


#Advanced Map: Passing List of functions directly
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)
# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]

#Reduce performs some computation on a list and returns the result. E.g: Product/Sum of all the elements in the list

from functools import reduce
product = reduce((lambda x, y: x + y), [1, 2, 3, 4])
print(product)