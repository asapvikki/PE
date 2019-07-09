from collections import defaultdict 
graph = defaultdict(list)
name_pairs = input()
name_pairs = name_pairs.split()
name_pairs = [str(a) for a in name_pairs]
i = 0
temp = 0
for a in name_pairs:
	if i%2==0:
		i = i+1
	else :
		graph[a].append(name_pairs[i-1])
		graph[name_pairs[i-1]].append(a)
		i=i+1
visited = []
def dfs (graph,node):
	global visited
	if node not in visited:
		visited.append(node)
		for x in graph[node]:
			dfs(graph,x)

count = 0
for x in name_pairs:
	if x not in visited:
		count = count + 1
		dfs(graph,x)

print(count)

def dfs_check(graph,node1,node2):
	global visited
	
	if node1 not in visited:
		visited.append(node1)
		for x in graph[node1]:
			if x == node2:
				return True
			dfs_check(graph,x,node2)
	return False

check_pairs = input()
check_pairs = check_pairs.split()
check_pairs = [str(a) for a in check_pairs]
visited = []
ans = dfs_check(graph,check_pairs[0],check_pairs[1])
print(ans)
