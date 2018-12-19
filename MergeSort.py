def conquer(A, beg, mid, end):
	arr1 = A[beg:(mid+1)]#Upper bound excluded
	arr2 = A[(mid+1):end+1]

	i,j=0,0
	k=0
	while  i<len(arr1) and j<len(arr2):
		if arr1[i]<arr2[j]:
			A[beg+k]=arr1[i]
			k+=1
			i+=1
		else:
			A[beg+k]=arr2[j]
			k+=1
			j+=1
	while i<len(arr1):
		A[beg+k]=arr1[i]
		k+=1
		i+=1

	while j<len(arr2):
		A[beg+k]=arr2[j]
		k+=1
		j+=1

	return A

def divide(A, beg, end):
	# print(beg, end)
	if(beg>=end):
		return
	mid = (beg+end)//2
	divide(A, beg, mid)
	divide(A, mid+1, end)
	return conquer(A,beg,mid,end)
arr = list(map(int, input().strip().split()))
n = len(arr)
print (divide(arr, 0, n-1))
# beg = 1
# end = n-2
# mid = (beg+end)//2
# conquer(arr,beg,mid,end)