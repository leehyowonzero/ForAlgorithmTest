from collections import deque

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]
def bfs(x,y):
	q = deque()
	q.append([x,y])
	while(q):
		x, y = q.popleft()
		for d in range(8):
			nx = x + dx[d]
			ny = y + dy[d]
			if not (0 <= nx< h and 0 <= ny < w):
				continue
			if(Map[nx][ny] == 1):
				Map[nx][ny] = 0
				q.append([nx,ny])
	return 1
while(True):
		# 입력
		w, h = map(int,input().split())
		if(w == 0 and h == 0):
			break
		Map = []
		for _ in range(h):
			Map.append(list(map(int, input().split())))
		
		ans = 0
		for i in range(h):
			for j in range(w):
				if(Map[i][j] == 1):
					ans += bfs(i,j)
					Map[i][j] = 0
		print(ans)