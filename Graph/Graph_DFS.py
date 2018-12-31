'''
	Undirected Graph, but still using weight 1 for all for weighted graph practice.
	1 - indexed Adjacency list
'''
parent=[]
color=[]
dist=[]
finish=[]
time=0
def print_adj_list(adj_list, n):
	for i in range(1, n+1):
		print(i,':',end='')
		for val in adj_list[i]:
			print(val,'->', end='')
		print()

def dfs_visit(adj_list,u):
	global parent, color, dist, finish, time
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
	print(u,end = ' finished ')

def dfs(adj_list, n):
	global parent, color, dist, finish, time
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
	adj_list[v].append([u,1])#Undirected!
	i+=1

print_adj_list(adj_list, n)
# bfs(adj_list, n, 2)
dfs(adj_list, n)





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
