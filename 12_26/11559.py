from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def show():
	for i in range(12):
		for j in range(6):
			print(Map[i][j], end = ' ')
		print()
	print()

def dropdown():
	for i in range(6):
		for j in range(11,-1,-1):
			if(Map[j][i] != '.'):
				k = j
				while(k+1 < 12 and Map[k+1][i] == '.'):
					k += 1
				Map[j][i], Map[k][i] = Map[k][i], Map[j][i]
def check():
	global ans
	flag = False
	for i in range(12):
		for j in range(6):
			if(Map[i][j] != '.'):
				visited = [[0 for _ in range(6)] for _ in range(12)]
				candi = []
				q = deque()
				q.append([i,j,Map[i][j]])
				candi.append([i,j])
				visited[i][j] = 1
				while q:
					x, y, color = q.popleft()
					for d in range(4):
						nx = x + dx[d]
						ny = y + dy[d]
						if not (0<= nx<12 and 0<= ny <6):
							continue
						if(visited[nx][ny] == 1):
							continue
						if(Map[nx][ny] == color):
							q.append([nx,ny,color])
							candi.append([nx,ny])
							visited[nx][ny] = 1
				if(len(candi) >= 4):
					for el in candi:
						x, y = el
						Map[x][y] = '.'
					flag = True

	if flag:
		ans += 1
		dropdown()
		check()
	
Map = []
ans = 0
for _ in range(12):
	Map.append(list(input()))
check()
print(ans)