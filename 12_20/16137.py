from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def checkMap():
	for i in range(n):
		for j in range(n):
			if(Map[i][j] == 0): # 절벽일 때
				for d in range(4):
					otherside = (d+1)%4
					nx1 = i + dx[d]
					ny1 = j + dy[d]
					nx2 = i + dx[otherside]
					ny2 = j + dy[otherside]
					if not (0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n):
						continue
					if(Map[nx1][ny1] == 0 and Map[nx2][ny2] == 0):
						Map[i][j] = -1
						break
def bfs():
	global ans
	q = deque()
	q.append([0,0,False, False,0])
	visited[0][0] = 1
	while q :
		x, y, state, used, cnt = q.popleft() # 좌표, 그전에 다리를 건넜는지, 경과 시간

		if(x == n-1 and y == n-1):
			ans = min(ans, cnt)
			continue
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if not (0 <= nx < n and 0 <= ny < n):
				continue
			if(used == False):
				if(visited[nx][ny] <= cnt + 1):
					continue
				if(Map[nx][ny] == 1):
					visited[nx][ny] =  cnt + 1
					q.append([nx, ny, False, used, cnt + 1])
				elif(Map[nx][ny] == -1):
					continue
				elif(Map[nx][ny] == 0):
					if(state == True): # 그전턴에 다리를 건넘
						continue
					else: # 그전턴에 다리를 안건넘
						nextcnt = cnt + (m - cnt % m)
						visited2[nx][ny] = nextcnt
						q.append([nx, ny, True, True, nextcnt])
				else:
					if(state == True): # 그전턴에 다리를 건넘
						continue
					else: # 그전턴에 다리를 안건넘
						nextcnt = cnt + (Map[nx][ny] - cnt % Map[nx][ny])
						visited[nx][ny] = nextcnt
						q.append([nx, ny, True, used, nextcnt])
			else:
				if(visited2[nx][ny] <= cnt + 1):
					continue
				if(Map[nx][ny] == 1):
					visited2[nx][ny] =  cnt + 1
					q.append([nx, ny, False, used, cnt + 1])
				elif(Map[nx][ny] == -1):
					continue
				elif(Map[nx][ny] == 0):
					if(state == True): # 그전턴에 다리를 건넘
						continue
				else:
					if(state == True): # 그전턴에 다리를 건넘
						continue
					else: # 그전턴에 다리를 안건넘
						nextcnt = cnt + (Map[nx][ny] - cnt % Map[nx][ny])
						visited2[nx][ny] = nextcnt
						q.append([nx, ny, True, used, nextcnt])
		
			


n, m = map(int,input().split())
Map = []
ans = 100000
for _ in range(n):
	Map.append(list(map(int,input().split())))
visited = [[100000 for _ in range(n)] for _ in range(n)]
visited2 = [[100000 for _ in range(n)] for _ in range(n)]
checkMap()
bfs()
# print()
# for i in range(n):
# 	for j in range(n):
# 		print(visited[i][j], end = ' ')
# 	print()
print(ans)