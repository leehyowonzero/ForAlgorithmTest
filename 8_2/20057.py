# 3 ≤ N ≤ 499
# N은 홀수
# 0 ≤ A[r][c] ≤ 1,000
# 가운데 칸에 있는 모래의 양은 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
winddir = [
	[(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,1,0.01),(1,1,0.01),
              (-1,-1,0.1),(1,-1,0.1),(0,-2,0.05), (0,-1,1)],
	[(-1,-1,0.01),(-1,1,0.01),(0,-1,0.07),(0,1,0.07),(0,-2,0.02),(0,2,0.02),
                 (1,-1,0.1),(1,1,0.1),(2,0,0.05),(1,0,1)],
	[(-1,0,0.07),(-2,0,0.02),(1,0,0.07),(2,0,0.02),(-1,-1,0.01),(1,-1,0.01),
              (-1,1,0.1),(1,1,0.1),(0,2,0.05),(0,1,1)],
	[(-1,-1,0.1),(-1,1,0.1),(0,1,0.07),(0,-1,0.07),(1,-1,0.01),(1,1,0.01),
               (-2,0,0.05),(0,-2,0.02),(0,2,0.02),(-1,0,1)]
]



# 모래 움직이기 함수
def movesand(x, y, direction):
	# print("움직였소")
	global ans
	cnt = 0
	for el in winddir[direction]:
		if(el[2] == 1):
			Map[x][y] -= cnt
			if not(0 <= x+el[0] < n and 0 <= y+el[1]< n):
				ans += int(Map[x][y] * el[2])
				Map[x][y] = 0
				continue
			Map[x+el[0]][y+el[1]] += int(Map[x][y])
			Map[x][y] = 0
		else:
			if not(0 <= x+el[0] < n and 0 <= y+el[1]< n):
				ans += int(Map[x][y] * el[2])
				cnt += int(Map[x][y] * el[2])
				continue
			Map[x+el[0]][y+el[1]] += int(Map[x][y] * el[2])
			cnt += int(Map[x][y] * el[2])
		

# 입력
n = int(input())
Map = []
for _ in range(n):
	Map.append(list(map(int,input().split())))
global ans
visited = [ [0 for _ in range(n)]for _ in range(n)]
ans = 0
# 모래를 옮긴다 시작지점 : (n//2, n//2)
# 초기 움직이는 길이 1
# 모래를 움직이는 방향 2 턴마다 길이가 1씩 늘어나고 방향은 계속 반시계로 회전
# 움직이는 횟수 = 2*n - 1
movelen = 1
movedir = 0  # left
x, y = n//2, n//2
for i in range(0, 2*n-1, 1):
	for _ in range(movelen):
		visited[x][y] = i
		if not (0 <= x + dx[movedir] < n and 0<= y + dy[movedir] < n):
			continue
		x = x + dx[movedir]
		y = y + dy[movedir]
		movesand(x, y, movedir)
	if(i % 2 == 1):
		movelen += 1
	movedir	= (movedir + 1) % 4
print(ans)
# for i in range(n):
# 	for j in range(n):
# 		print(visited[i][j], end = " ")
# 	print()