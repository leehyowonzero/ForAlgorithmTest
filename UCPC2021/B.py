from collections import deque

dx = [0,-1, 0 , 1]
dy = [1, 0, -1, 0]

def aftercheck(check):
	x , y = check[0]
	pivot = after[x][y]
	for i in range(1,len(check)):
		if(pivot != after[check[i][0]][check[i][1]]):
			return False
	for el in check:
		after[el[0]][el[1]] = before[el[0]][el[1]]
	return True

def bfs(i, j):
	visited = [[0 for _ in range(m)] for _ in range(n)]
	check = []
	q = deque()
	q.append([i,j])
	check.append([i,j])
	while(q):
		x, y = q.popleft()
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if not(0<=nx<n and 0<=ny <m):
				continue
			if(visited[nx][ny]!= 0):
				continue
			if(before[x][y] == before[nx][ny]):
				q.append([nx,ny])
				check.append([nx,ny])
				visited[nx][ny] = 1

	return aftercheck(check)
n, m = map(int,input().split())
before = []
for _ in range(n):
	before.append(list(map(int,input().split())))
after = []
for _ in range(n):
	after.append(list(map(int,input().split())))
cnt = 0
for i in range(n):
	for j in range(m):
		if before[i][j] != after[i][j] :
			if(cnt == 0):
				if(bfs(i,j)):
					cnt += 1
				else:
					print("NO")
					quit(0)
			else:
				print("NO")
				quit(0)
print("YES")
			