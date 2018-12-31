'''
	Directed Acyclic Graph, but still using weight 1 for all for weighted graph practice.
	1 - indexed Adjacency list
'''
parent=[]
color=[]
dist=[]
finish=[]
order = []
time=0
def print_adj_list(adj_list, n):
	for i in range(1, n+1):
		print(i,':',end='')
		for val in adj_list[i]:
			print(val,'->', end='')
		print()

def dfs_visit(adj_list,u):
	global parent, color, dist, finish, time, order
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
	order.insert(0,u)
	print(u,end = ' finished ')

def dfs(adj_list, n):
	global parent, color, dist, finish, time, order
	parent = [0]*(n+1)
	color = [0]*(n+1)
	dist = [float("inf")]*(n+1)
	finish = [0]*(n+1)
	time = 0
	for i in range(1,n+1):
		if color[i]==0:
			dfs_visit(adj_list,i)
	print()



n = int(input().strip())
no_edges = int(input().strip())

#1-indexed
adj_list = [[] for i in range(n+1)]
i=0
while i<no_edges:
	u, v = map(int, input().strip().split())
	adj_list[u].append([v,1])
	i+=1

print_adj_list(adj_list, n)
# bfs(adj_list, n, 2)
dfs(adj_list, n)
print('topological sort:', order)





#Sample Input
'''
5
5
1 4
2 1
3 2
4 5


'''
