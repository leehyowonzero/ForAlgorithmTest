# 모든 구름이 di 방향으로 si칸 이동한다.
# 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
# 구름이 모두 사라진다.
# 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
# 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
# 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
# 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.

import sys

input = sys.stdin.readline



def rainning(cloud):
	increasedpos = []
	for el in cloud:
		x = el[0]
		y = el[1]
		Map[x][y] += 1
		increasedpos.append([x, y])
	return increasedpos
		
def watercopy(arr):
	dx = [-1,-1,1,1]
	dy = [-1,1,-1,1]
	for el in arr:
		power = 0
		x = el[0]
		y = el[1]
		for d in range(4):
			nx = x + dx[d]
			ny = y + dy[d]
			if not (0 <= nx< n and 0<= ny < n):
				continue
			if(Map[nx][ny] > 0):
				power += 1
		Map[x][y] += power
def confirm(x, y, exception):
	for el in exception:
		if(x == el[0] and y == el[1]):
			return False
	return True

def check(exception):
	ret = []
	for i in range(n):
		for j in range(n):
			if(Map[i][j] >= 2 and confirm(i,j, exception)):
				Map[i][j] -= 2
				ret.append([i, j])
	return ret
				

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]
n, m = map(int,input().split())
Map = []
for _ in range(n):
	Map.append(list(map(int,input().split())))
command = []
for _ in range(m):
	command.append(list(map(int,input().split())))
cloud = [(n-1, 0), (n-1,1), (n-2, 0), (n-2, 1)] # 기본 구름 위치
for i in range(m):
	# 구름 움직이기
	for j in range(len(cloud)):
		cloud[j] = ((cloud[j][0] +  command[i][1]*dx[command[i][0]])%n, (cloud[j][1] + command[i][1]*dy[command[i][0]])%n)	
	increasedpos = rainning(cloud)
	watercopy(increasedpos)
	cloud = check(increasedpos)


ans = 0
for i in range(n):
	for j in range(n):
		ans += Map[i][j]
print(ans)
