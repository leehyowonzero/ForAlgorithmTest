from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(x,y):
	q = deque()
	q.append([x,y])
	while(q):
		x, y = q.popleft()
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if not (0 <= nx< n and 0 <= ny < m):
				continue
			if(Map[nx][ny] == 1):
				Map[nx][ny] = 0
				q.append([nx,ny])
	return 1
# 입력
t = int(input())
for _ in range(t):
	ans = 0
	m, n ,k = map(int,input().split())
	Map = [[0 for _ in range(m)] for _ in range(n)]
	for _ in range(k):
		y, x = map(int,input().split())
		Map[x][y] = 1
	for i in range(n):
		for j in range(m):
			if(Map[i][j] == 1):
				Map[i][j] = 0
				ans += bfs(i,j)
				
	print(ans)