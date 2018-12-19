def left_(i):
	return 2*i
def right_(i):
	return 2*i+1

def max_heapify(a, i, n):
	largest = i
	left = left_(i) 
	right = right_(i)
	if left<=n and a[left]>a[largest]:
		largest = left
	if right<=n and a[right]>a[largest]:
		largest = right
	if largest!=i:
		a[largest], a[i]= a[i], a[largest]
		# print(a)
		a = max_heapify(a,largest,n)
	return a
def build_heap(a, n):
	for i in range(n//2,0,-1):
		a = max_heapify(a, i, n)
	return a

def heap_sort(a,n):
	for i in range(n,2,-1):
		a[i], a[1] = a[1], a[i]
		n-=1
		a = max_heapify(a,1,n)
	return a
arr = list(map(int, input().strip().split()))
n = len(arr)
arr.insert(0,0)
print('before',arr)
arr = max_heapify(arr, 1, n)
print('last:',arr)
print(build_heap(arr,n)[1:])
print(heap_sort(arr, n)[1:])
print(arr)