from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(now, fire):
	visited = [[0 for _ in range(w)] for _ in range(h)]
	q = deque()
	for el in fire:
		q.append([el[0], el[1] , 1])
	x, y = now[0], now[1]
	q.append([x,y, 0])
	turn = 1 
	while q:
		turnlen = len(q)
		for _ in range(turnlen):
			x, y, isfire = q.popleft()
			for d in range(4):
				nx = x + dx[d]
				ny = y + dy[d]
				# 불일때
				if(isfire):
					if not (0 <= nx < h and 0 <= ny < w):
						continue
					if(Map[nx][ny] == '.'):
						Map[nx][ny] = '*'
						q.append([nx,ny,1])
				# 사람일때
				else:
					if not (0 <= nx < h and 0 <= ny < w):
						print(turn)
						return 
					if(Map[nx][ny] == '.' and visited[nx][ny] == 0):
						q.append([nx,ny,0])
						visited[nx][ny] =  1
		turn += 1
	print("IMPOSSIBLE")


# 입력
t = int(input())
for _ in range(t):
	w, h = map(int,input().split())
	Map = []
	for _ in range(h):
		Map.append(list(input()))
	
	# 상근이와 불의 위치 찾기
	fire = []
	for i in range(h):
		for j in range(w):
			if(Map[i][j] == '*'):
				fire.append([i,j])
			elif(Map[i][j] == '@'):
				player = [i, j]
				Map[i][j] = '.'
	bfs(player,fire)