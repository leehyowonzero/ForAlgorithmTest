from collections import deque

dx = [0 ,0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
	turnon = [[0 for _ in range(N+1)] for _ in range(N+1)]
	visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
	ans = 0
	q = deque()
	q.append((x, y))
	ans += 1 
	visited[1][1] = 1
	turnon[1][1] = 1
	while q:
		x, y = q.popleft()
		for el in light[x][y]:
			nowx, nowy = el[0], el[1]
			if(turnon[nowx][nowy] == 0):
				ans += 1
			turnon[nowx][nowy] = 1
			for d in range(4):
				nx = nowx + dx[d]
				ny = nowy + dy[d]
				if not (0 < nx <= N and 0 < ny <= N):
					continue
				if(visited[nx][ny] == 1 and visited[nowx][nowy] == 0):
					q.append((nowx, nowy))
					visited[nowx][nowy] = 1
					break
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if not (0 < nx <= N and 0 < ny <= N):
				continue
			if(visited[nx][ny] == 0 and turnon[nx][ny] == 1):
				q.append((nx, ny))
				visited[nx][ny] = 1
	return ans
			


N, M = map(int,input().split())
light = [[[] for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
	x, y, a, b = map(int,input().split())
	light[x][y].append((a, b))

print(bfs(1,1))
