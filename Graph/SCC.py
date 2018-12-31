'''
	Directed Graph, but still using weight 1 for all for weighted graph practice.
	1 - indexed Adjacency list

	Algorithm:
	1) Create an empty stack ‘S’ and do DFS traversal of a graph. In DFS traversal, after calling recursive DFS for adjacent vertices of a vertex, 
	push the vertex to stack.
	2) Reverse directions of all arcs to obtain the transpose graph.
	3) One by one pop a vertex from S while S is not empty. Let the popped vertex be ‘v’. 
	Take v as source and do DFS (call DFS_visit(v)). The DFS starting from v prints strongly connected component of v. 
	(One by one popped from stack).

'''
parent=[]
color=[]
dist=[]
finish=[]
stack = []
time=0
def print_adj_list(adj_list, n):
	for i in range(1, n+1):
		print(i,':',end='')
		for val in adj_list[i]:
			print(val,'->', end='')
		print()

def dfs_visit(adj_list,u):
	global parent, color, dist, finish, time, stack
	print(u,end = ' ')
	time+=1
	dist[u]=time
	color[u]=1
	for v,weight in adj_list[u]:
		if color[v]==0:
			parent[v]=u
			dfs_visit(adj_list,v)
	color[u]=2
	time+=1
	finish[u]=time
	stack.append(u)
	# print(u,end = ' finished ')

def dfs(adj_list, n, scc=False):
	global parent, color, dist, finish, time, stack
	parent = [0]*(n+1)
	color = [0]*(n+1)
	dist = [float("inf")]*(n+1)
	finish = [0]*(n+1)
	time = 0

	if scc==True:
		while len(stack)!=0:
			i=stack.pop()
			if color[i]==0:
				print('SCC:',end=' ')
				dfs_visit(adj_list,i)
				print()

	else:
		for i in range(1,n+1):
			if color[i]==0:
				dfs_visit(adj_list,i)
		print()



n = int(input().strip())
no_edges = int(input().strip())

#1-indexed
adj_list = [[] for i in range(n+1)]
rev_list = [[] for i in range(n+1)]
i=0
while i<no_edges:
	u, v = map(int, input().strip().split())
	adj_list[u].append([v,1])
	rev_list[v].append([u,1])
	i+=1

print_adj_list(adj_list, n)
# bfs(adj_list, n, 2)
dfs(adj_list, n)
print('stack:', stack)
dfs(rev_list, n, scc=True)





#Sample Input
'''
5
5
1 3
1 4
2 1
3 2
4 5



'''
