'''
	Undirected Graph, but still using weight 1 for all for weighted graph practice.
	1 - indexed Adjacency list
'''
def print_adj_list(adj_list, n):
	for i in range(1, n+1):
		print(i,':',end='')
		for val in adj_list[i]:
			print(val,'->', end='')
		print()

def bfs(adj_list, n, src):
	parent = [0]*(n+1)
	color = [0]*(n+1)
	dist = [float("inf")]*(n+1)
	import queue
	q = queue.Queue()
	color[src] = 1 #White to gray, marked vistited/discovered
	dist[src] = 0 #Source Distance
	parent[src] = 0 #NIL Parent 
	q.put(src)
	while not q.empty():
		u = q.get()
		print(u,end=" ")
		for v, weight in adj_list[u]:
			if color[v] == 0:
				color[v] = 1 #Gray, just discovered
				parent[v] = u
				dist[v] = dist[u] + 1 
				q.put(v)
		color[u]=2 # Explored
	print()
	print('dist:', dist[1:])
	print('parent:', parent[1:])
	print('color', color[1:])

	def print_path(adj_list, src, v):# v: vertex
		if v==src:
			print(src, end=' ')
		elif parent[v]==0:#NIL parent
			print('No path from',src,'to',v,'exists in the BFS tree.')
		else:
			print_path(adj_list, src, parent[v])
			print(v, end=' ')
	print_path(adj_list, 1, 8)#src is fixed src
	print()



n = int(input().strip())
no_edges = int(input().strip())

#1-indexed
adj_list = [[] for i in range(n+1)]
i=0
while i<no_edges:
	u, v = map(int, input().strip().split())
	adj_list[u].append([v,1])
	adj_list[v].append([u,1])#Undirected!
	i+=1

print_adj_list(adj_list, n)
bfs(adj_list, n, 2)






#Sample Input
'''
8
10
1 2
1 3
2 4
4 5
4 6
5 6
5 7
6 7
6 8
7 8


'''
