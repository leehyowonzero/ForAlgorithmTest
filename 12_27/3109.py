dx = [-1,0,1]
dy = [1,1,1]

def show():
	for i in range(r):
		for j in range(c):
			print(Map[i][j], end = ' ')
		print()
	print()

def go(start):
	global ans
	x, y = start
	Map[x][y] = 'x'
	if(y == c-1):
		ans += 1
		return True
	for d in range(3):
		nx = x + dx[d]
		ny = y + dy[d]
		if not (0 <= nx < r and 0 <= ny < c):
			continue 
		if(Map[nx][ny] == 'x'):
			continue
		if(go([nx,ny]) == True):
			return True
	return False



r, c = map(int,input().split())
Map = []
ans = 0
for _ in range(r):
	Map.append(list(input()))
for i in range(0, r):
	# show()
	start = [i, 0]
	if(Map[start[0]][start[1]] == '.'):
		go(start)
print(ans)