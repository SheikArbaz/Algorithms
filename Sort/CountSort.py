k=100

def count_sort(arr):

	n = len(arr)
	count = [0]*k

	#count[i]: no. of elements equal to i
	for i in range(0,n):
		count[arr[i]]+=1

	#count[i]: no. of elements less or equal to i
	for i in range(1,k):
		count[i]+=count[i-1]

	#Fix the position of A[i]: the value C[A[i]]is the correct final position A[i] in the output array, 
								#since there are C[A[i]]elements less than or equal A[i]
	b = [0]*(n)
	for i in range(n-1,-1,-1):
		b[count[arr[i]]-1] = arr[i]
		count[arr[i]]-=1
	return b

def count_sort2(arr, exp):
	n = len(arr)
	count = [0]*k

	for i in range(0,n):
		count[(arr[i]//exp)%10]+=1


	for i in range(1,k):
		count[i]+=count[i-1]

	# print(count)
	b = [0]*(n)
	for i in range(n-1,-1,-1):
		# print(i,arr[i])
		b[count[(arr[i]//exp)%10]-1] = arr[i]
		count[(arr[i]//exp)%10]-=1
	return b
def radix_sort(arr):
	mx = max(arr)
	exp = 1
	while mx//exp>1:
		arr = count_sort2(arr, exp)
		exp*=10
	return arr

arr = list(map(int, input().strip().split()))
print(radix_sort(arr))
