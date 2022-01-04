from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(start):
	global island_num
	q = deque([start])
	while q:
		x, y= q.popleft()
		arr[x][y] = island_num
		visited[x][y] = False
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] and visited[nx][ny]:
				arr[nx][ny] = island_num
				visited[nx][ny] = False
				q.append([nx, ny])

def CheckDistance(x, y):
	for d in range(4):
		k = 0
		nx = x + dx[d]
		ny = y + dy[d]
		if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
			while True:
				k += 1
				nx += dx[d]; ny += dy[d]
				if not 0 <= nx < N or not 0 <= ny < M:
					break
				if arr[nx][ny] != 0:
					if k >= 2 and island_distance[arr[x][y]][arr[nx][ny]] > k: 
						island_distance[arr[x][y]][arr[nx][ny]] = k
					break

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[True for _ in range(M)] for _ in range(N)]
island_num = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] and visited[i][j]:
            bfs([i, j])
            island_num += 1

island_distance = [[11 for _ in range(island_num)]  for _ in range(island_num)]

for i in range(N):
    for j in range(M):
        if arr[i][j]:
            CheckDistance(i, j)

edge = []
for i in range(1, island_num - 1):
    for j in range(1, island_num):
        if island_distance[i][j] != 11:
            edge.append((i, j, island_distance[i][j]))

edge.sort(key=lambda x: x[2])


p = [x for x in range(island_num)]

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]
def union(u,v):
	root1 = find(u)
	root2 = find(v)
	p[root2] = root1

tree_edges = 0
mst_cost = 0
mst = []
while True:
	if(tree_edges == island_num-2):
		break
	if not(edge):
		print(-1)
		exit(0)
	u, v, wt = edge.pop(0)
	if(find(u) != find(v)):
		union(u, v)
		mst.append((u, v))
		mst_cost += wt
		tree_edges += 1
print(mst_cost)