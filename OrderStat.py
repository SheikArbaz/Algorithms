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

def kth_smallest(A, beg, end, i):
	if(beg==end):
		# print('equal case')
		return A[beg]
	pivot_index = get_pivot_index(A, beg, end)
	k = pivot_index-beg+1 #no.of elements less than A[pivot_index] in the array A[beg:end+1] including itself
	#2. k = pivot_index #no.of elements less than A[pivot_index] in the complete actual array A[0:end+1] including itself

	print(A, k, i)
	if k==i:
		return A[pivot_index]
	elif i<k:
		return kth_smallest(A, beg, pivot_index-1, i)
	else:
		return kth_smallest(A, pivot_index+1, end, i-k) #call for i-k in A[beg:end+1] as k elements are aready in the lower part
		#2. return kth_smallest(A, pivot_index+1, end, i) #call for i as we're comparing in the complete array A[0:end+1] 

# arr = list(map(int, input().strip().split()))
# k-th smallest element
# k = int(input())
arr = [7, 10, 4, 3, 20, 15]
k = 1

n = len(arr)
print(kth_smallest(arr, 0, n-1, 6))
# print(arr)