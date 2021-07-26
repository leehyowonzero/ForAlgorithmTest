import sys

dx = [0,-1,1,0,0] # 1~4 위 아래 왼쪽 오른쪽
dy = [0,0,0,-1,1]

def check(arr):
	cnt = 0
	for i in range(len(arr)):
		if(arr[i] != None):
			cnt += 1
	if(cnt == 1):
		return True
	else:
		return False
# 입력
n, m, k = map(int,input().split())
Map = []
for _ in range(n):
	Map.append(list(map(int,input().split())))
direction = list(map(int,input().split()))  
shark_num = m # 상어가 몇마리인지, 맵상의 상어와 인덱스  - 1 차이
priority = [[] for _ in range(shark_num)]
for i in range(shark_num): # 각 i 번 상 어의 우선순위가 나와있음   
	for _ in range(4):
		priority[i].append(list(map(int,input().split())))

# 각 상어의 위치를 저장할 리스트 생성
shark = [[] for _ in range(shark_num)]
for i in range(n):
	for j in range(n):
		if(Map[i][j] != 0):
			shark[Map[i][j]-1] = [i,j]
smell = [[None for _ in range(n)] for _ in range(n)]
times = 1
while(True):
	# print(times)
	# print(*direction)
	# for i in range(n):
	# 	for j in range(n):
	# 		print(Map[i][j], end = ' ')
	# 	print()
	# for i in range(n):
	# 	for j in range(n):
	# 		print(smell[i][j], end = ' ')
	# 	print()
	if(times > 1000):
		print("-1")
		sys.exit(0)
 	#맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
	for index, el in enumerate(shark):
		if(el != None):
			smell[el[0]][el[1]] = [index+1,k]
	
	
	# 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.
	#각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 
	for index, el in enumerate(shark):
		if(el == None):
			continue
		flag = False
		nowsharkpri = priority[index][direction[index]-1]
		x, y = el[0], el[1]
		for d in nowsharkpri:
			nx = x + dx[d]
			ny = y + dy[d]
			if not ( 0 <= nx < n and 0 <= ny < n):
				continue
			if (smell[nx][ny] != None):
				continue
			# 냄세 없는 칸이 있어서 방향잡고 움직이기.
			# print(index + 1,d,"방향으로 움직이기")
			if(Map[nx][ny] != 0): # 이미 다른 물고기가 자리 잡음
				Map[x][y] = 0
				shark[index] = None
				flag = True
				break

			Map[nx][ny] = index + 1
			Map[x][y] = 0
			direction[index] = d
			shark[index] = [nx,ny]
			flag = True # 이동함을 의미
			break
		#그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.
		if not (flag):
			for d in nowsharkpri:
				nx = x + dx[d]
				ny = y + dy[d]
				if not ( 0 <= nx < n and 0 <= ny < n):
					continue
				if (smell[nx][ny][0] == index + 1):
					# 자신이랑 같은 냄세 칸이 있어서 방향잡고 움직이기.
					Map[nx][ny] = index + 1
					Map[x][y] = 0
					direction[index] = d
					shark[index] = [nx,ny]
					flag = True # 이동함을 의미
					break
		if(flag == False): # 결국 이동 못함
			Map[x][y] = 0
			shark[index] = None
	#모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
	
	# 상어가 한마리만 남았는지 체크
	if(check(shark)):
		break
	# 여기서 상어의 냄세를 하나씩 줄이자
	for i in range(n):
		for j in range(n):
			if(smell[i][j] != None):
				smell[i][j][1] -= 1
				if(smell[i][j][1] == 0):
					smell[i][j] = None
	times += 1
print(times)
