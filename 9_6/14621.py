def find(parent, x):
	if(parent[x] != x):
		parent[x] = find(parent,parent[x])
	return parent[x]

def union(parent, a, b):
	a = find(parent, a)
	b = find(parent, b)
	if(a < b):
		parent[b] = a
	else:
		parent[a] = b
	
v, e = map(int,input().split())
parent = [0 for i in range(v+1)]
edge = []
ans = 0
gender = [0]
for i in range(1, v+1):
	parent[i] = i
gender.extend(list(input().split()))
for _ in range(e):
	a, b, cost = map(int,input().split())
	edge.append((cost, a, b))

edge.sort()
cnt = 0
for el in edge:
	cost, a, b = el
	if(find(parent, a) != find(parent, b) and gender[a] != gender[b]):
		union(parent, a, b)
		ans += cost
		cnt += 1

if(cnt == v-1):
	print(ans)
else:
	print("-1")	
