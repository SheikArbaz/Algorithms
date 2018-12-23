from functools import reduce
def insertion_sort(arr):
	n = len(arr)
	i = 1
	for i in range(1, n):
		j = i-1
		key = arr[i]
		while j>=0 and arr[j]>key:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key
	#No need to return: inplace as list is an object
	# return arr
def bucket_sort(A):
	n = len(A)
	#Create an array of lists
	B=[[] for i in range(n)]

	#append A[i] to the list at n*val in B.
	for val in A:
		B[int(n*val)].append(val)
	print(B)
	for val in B:
		insertion_sort(val)
	return reduce((lambda x,y: x+y), B)


#Sample: 0.78 0.12 0.13 0.5 0.6 0.51 0.4 0.9 0.1 0.23
arr = list(map(float, input().strip().split()))
print(bucket_sort(arr))