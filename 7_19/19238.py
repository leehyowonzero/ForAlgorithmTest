#현재 위치에서 가장 가까운 택시를 찾는 bfs를 통해 태울 사람을 정하고
# 그 사람을 태우러 간 후 태운사람의 도착지까지 이동 이때 연료량 확인
# 도착지까지 데려다주면 연료량 확인, 통과하면 연료를 추가해주고  Map에 승객 좌표 없앰 
# 위 과정 반복
from collections import deque
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def bfs_for_goal(guestinfo):
	visited = [[0 for _ in range(n)] for _ in range(n)]
	start = guestinfo[0:2]
	q = deque()
	q.append(start)
	cnt = 1 #소모 연료
	while q:
		turn = len(q)
		for x in range(turn):
			x, y = q.popleft()
			for d in range(4):
				nx = x + dx[d]
				ny = y + dy[d]
				if not(0 <= nx < n and 0 <= ny < n):
					continue
				if(visited[nx][ny] != 0 or Map[nx][ny] == 1):
					continue
				if(nx == guestinfo[2] and ny == guestinfo[3]):
					return nx, ny, cnt
				else:
					q.append([nx,ny])
				visited[nx][ny] = 1
		cnt += 1
	return 0, 0 , 5000000
def searchinfo(x,y):
	for i in range(len(guest)):
		if(x == guest[i][0] and y == guest[i][1]):
			return i
def bfs_for_guest(start):
	
	if(Map[start[0]][start[1]] == 2):
		return searchinfo(start[0],start[1]), 0
	visited = [[0 for _ in range(n)] for _ in range(n)]
	q = deque()
	q.append(start)
	cnt = 1 #소모 연료
	while q:
		turn = len(q)
		candi = []
		for x in range(turn):
			x, y = q.popleft()
			for d in range(4):
				nx = x + dx[d]
				ny = y + dy[d]
				if not(0 <= nx < n and 0 <= ny < n):
					continue
				if(visited[nx][ny] != 0 or Map[nx][ny] == 1):
					continue
				
				if(Map[nx][ny] == 2):
					# 고객정보 추가
					candi.append([nx,ny])
				else:
					q.append([nx,ny])
				visited[nx][ny] = 1
		if(candi):
			candi.sort( key = lambda x : (x[0],x[1]))
			return searchinfo(candi[0][0],candi[0][1]), cnt
		cnt += 1
	return 0 , 5000000

# 입력
n, m, fuel = map(int,input().split())
Map = []
for _ in range(n):
	Map.append(list(map(int,input().split())))
start = list(map(int,input().split()))
global guest
guest = []
for _ in range(m):
	guest.append(list(map(int,input().split())))
#시작지점과 고객지점 배열 크기에 맞게 조정
for i in range(2):
	start[i] -= 1
for i in range(m):
	for j in range(4):
		guest[i][j] -= 1
# 고객 시작지점을 Map에 2로 표시
for el in guest:
	Map[el[0]][el[1]] = 2
# 모든 고객을 태우거나 연료가 모자를때까지 반복

ans = 0 #태운 승객
while(ans < m):
	# 현 위치(start)로부터 가장 가까운 고객 찾기 bfs를 통해  
	selectedguest, usedfuel = bfs_for_guest(start)
	fuel -= usedfuel
	if(fuel < 0):
		print("-1")
		break
	endx, endy, usedfuel = bfs_for_goal(guest[selectedguest])
	fuel -= usedfuel
	if(fuel < 0):
		print("-1")
		break
	fuel += usedfuel*2
	start = [endx, endy]
	ans += 1
	Map[guest[selectedguest][0]][guest[selectedguest][1]] = 0
	if(ans == m):
		print(fuel)
