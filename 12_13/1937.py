dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x, y):
	if dp[x][y]: 
		return dp[x][y]
	dp[x][y] = 1
	for d in range(4):
		nx = x + dx[d]
		ny = y + dy[d]
		if 0 <= nx < n and 0 <= ny < n:
			if Map[x][y] < Map[nx][ny]:
				dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
	return dp[x][y]
n = int(input())

Map = []
for _ in range(n):
	Map.append(list(map(int, input().split())))
dp = [[0 for _ in range(n)] for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)