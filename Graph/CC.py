'''
	Disjoint set for Connected Component
	1 - indexed senior, adj_list
'''
senior = [0] # 1-indexed, 0 neglected, the parent who represent a connected component
def print_adj_list(adj_list, n):
	for i in range(1, n+1):
		print(i,':',end='')
		for val in adj_list[i]:
			print(val,'->', end='')
		print()

def make_set(u):
	global senior
	senior.append(u)

def find_set(u):
	#To find the representative element.
	global senior
	if senior[u]!=u:
		return find_set(senior[u])
	return u

def union(senior_u,senior_v):
	#Connect two nodes by changing the parent of the u's parent
	global senior
	senior[senior_u]=senior[senior_v]
def connected_component(adj_list, n):
	global senior
	for i in range(1, n+1):
		make_set(i)
	print('senior:', senior[1:])
	for u in range(1, n+1):
		for v,_ in adj_list[u]:
			senior_u = find_set(u)
			senior_v = find_set(v)
			if(senior_u!=senior_v):
				union(senior_u,senior_v)

def is_same_component(u, v):
	global senior
	if find_set(u)==find_set(v):
		return True
	return False

n = int(input().strip())
no_edges = int(input().strip())

#1-indexed
adj_list = [[] for i in range(n+1)]
i=0
while i<no_edges:
	u, v = map(int, input().strip().split())
	adj_list[u].append([v,1])
	# adj_list[v].append([u,1])
	i+=1

print_adj_list(adj_list, n)

connected_component(adj_list, n)

print('senior:', senior[1:])

for i in range(1,n+1):
	for j in range(i+1,n+1):
		print(i,j,is_same_component(i,j))


#Sample Input
'''
6
4
1 2
4 2
3 5
1 6




'''
