arr = list(map(int, input().strip().split()))
n = len(arr)

for i in range(0,n):
	for j in range(0,n-i-1):
		if arr[j+1]<arr[j]:
			arr[j], arr[j+1] = arr[j+1],arr[j]

print(arr)