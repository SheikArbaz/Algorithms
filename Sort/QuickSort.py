def get_pivot_index(A, beg, end):
	pivot = A[end]
	i=beg-1 #i always point to the location just before the pivot index
	#j: traverse the array for movements
	for j in range(beg, end):
		if(A[j]<=pivot):
			#Less than pivot means: i has to bo moved one place more and the lesser value A[j] must be present there.
			i=i+1
			A[i],A[j]=A[j],A[i]
	#Finally, pivot in it's place
	A[i+1], A[end]=A[end], A[i+1]
	return i+1
def divide(A,beg,end):
	if beg<end:
		pivot = get_pivot_index(A,beg,end)
		divide(A,beg,pivot-1)
		divide(A,pivot+1,end)
arr = list(map(int, input().strip().split()))
n = len(arr)
divide(arr, 0, n-1)
print(arr)