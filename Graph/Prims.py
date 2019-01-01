'''
	Minimum Spanning Tree
	Prims: adj_list, senior: 1 - indexed
'''
senior = [0] # 1-indexed, 0 neglected
def print_adj_list(adj_list, n):
	for i in range(1, n+1):
		print(i,':',end='')
		for val in adj_list[i]:
			print(val,' ', end='')
		print()

def prims(adj_list, n, root=1):
	from queue import PriorityQueue
	q = PriorityQueue()
	'''
	Issue with "q" is we cannot update or remove a particular element. So, we'll create a new list D[] which stores minimal distance
	for each node and we'll maintain an mst_set too. When the expired node is extracted from the "q", we'll compare it with D[u]. D[u]<dist in case the expired "u" is
	extracted. It means "q" contains multiple copies but the expired ones will be neglected.
	'''
	D = [0] #1 - indexed, minimal distances
	parent = [0] #1 - indexed, parent to which v is connected included in MST
	for i in range(1,n+1):
		D.append(float('inf'))
		parent.append(0)
	D[root]=0
	parent[root]=1
	# print(D[1:])
	# print(parent[1:])
	for i in range(1,n+1):
		q.put((D[i], i))# (key, value) in tuple.priority is min  on key->(distance, node)

	ans1 = 0
	ans2 = []
	mst_set = set()
	while  not q.empty():# or len(mst_set)!=n
		val,u = q.get()
		if(val > D[u]): #expired ?
			continue
		# if u in mst_set: #If u is already in mst, they why to go for it again?
		# 	continue
		# else: # visited for the first time, add in mst
		mst_set.add(u)
		ans1+=val
		ans2.append([u,parent[u]])
		# print('val: ',val,'u: ',  u)
		for v,w in adj_list[u]:
			if w<D[v] and v not in mst_set: #To update the adjacent node it shouldn't be added to the mst_set
				D[v]=w
				parent[v]=u
				q.put((w, v))
	print('D:', D[1:])
	print('p:', parent[1:])
	print(ans1) # cost = sum(D1[:])
	print(ans2) #pairs

n = int(input().strip())
no_edges = int(input().strip())

#1-indexed
adj_list = [[] for i in range(n+1)]
i=0
while i<no_edges:
	u, v, w = map(int, input().strip().split())
	adj_list[u].append([v,w])
	adj_list[v].append([u,w])
	i+=1

print_adj_list(adj_list, n)

prims(adj_list, n)


#Sample Input
'''
9
14
1 2 4
1 8 8
2 3 8
2 8 11
3 4 7
3 6 4
3 9 2
4 5 9
4 6 14
5 6 10
6 7 2
7 8 1
7 9 6
8 9 7




'''
