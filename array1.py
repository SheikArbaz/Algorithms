from array import *
arr = array('i',[1,2,3,4,10])
# print(arr)

# for val in arr:
# 	print (val)

# print(arr[-2])

arr[0]=99

# print(arr)

arr.insert(100,200)#insert 200 at 100th position
print('index', arr.index(200))

print(arr)

arr.remove(3)
print(arr)

arr.append(233)
print(arr)

arr.insert(-2,404)
print(arr)

print(arr[1:3])

arr[2:4]=array('i',[8,9])
print(arr)