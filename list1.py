a=[1,2,'hello',2,3,4,5]
print(a)

a[5:7]=['a','9']
print(a)

del a[-1]#Delete by index

print(a)

a.remove(2)#Remove by element: removes first occurence
print(a)


#Remove all occurences of '2'
arr = [1,2,3,2,4,5,2]

print(list(filter(lambda num: num != 2, arr)))

