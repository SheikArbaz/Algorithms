'''
	Minimum Spanning Tree
	Kruskal: edge_list, senior:1 - indexed
'''
senior = [0] # 1-indexed, 0 neglected
def print_edge_list(edge_list):
	n = len(edge_list)
	for i in range(0, n):
		print(edge_list[i])		

def make_set(u):
	global senior
	senior.append(u)

def find_set(u):
	global senior
	if senior[u]!=u:
		return find_set(senior[u])
	return u

def union(senior_u,senior_v):
	global senior
	senior[senior_u]=senior[senior_v]

def kruskal(edge_list, n):
	global senior
	for i in range(1, n+1):
		make_set(i)
	print('senior:', senior[1:])
	mst_list = []
	mst_val = 0
	#For each edge: try to connect them to the same parent if not.
	for edge in edge_list:
			u,v,w = edge
			senior_u = find_set(u)
			senior_v = find_set(v)
			if(senior_u!=senior_v):
				#Connect it to the current MST
				union(senior_u,senior_v)
				mst_val+=w
				mst_list.append(edge)
	return mst_list, mst_val


n = int(input().strip())
no_edges = int(input().strip())

#1-indexed
edge_list = []
i=0
while i<no_edges:
	u, v, w = map(int, input().strip().split())
	edge_list.append([u,v,w])
	i+=1

print_edge_list(edge_list)

#Sort edge list by weights
edge_list = sorted(edge_list,key=lambda l:l[-1])
print(edge_list)

print(kruskal(edge_list, n))
# connected_component(edge_list, n)

# print('senior:', senior[1:])

# for i in range(1,n+1):
# 	for j in range(i+1,n+1):
# 		print(i,j,is_same_component(i,j))


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
