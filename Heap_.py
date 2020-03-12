
def get_left(i):
	return 2*i
def get_right(i):
	return 2*i+1

def max_heapify(a, i, n):
	largest = i
	left = get_left(i) 
	right = get_right(i)
	if left<=n and a[left]>a[largest]:
		largest = left
	if right<=n and a[right]>a[largest]:
		largest = right
	if largest!=i:
		a[largest], a[i]= a[i], a[largest]
		max_heapify(a,largest,n)
def build_heap(a, n):
	for i in range(n//2,0,-1):
		max_heapify(a, i, n)
		print(a)

def heap_sort(a,n):
	for i in range(n,1,-1):
		a[i], a[1] = a[1], a[i]
		n-=1
		max_heapify(a,1,n)


arr = list(map(int, input().strip().split()))
n = len(arr)
arr.insert(0,0)
print(arr)

print('build_heap------')
build_heap(arr,n)
print(arr)

print('heap_sort------')
heap_sort(arr, n)
print(arr)

print(n)
