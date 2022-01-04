from heapq import heappush, heappop
# import sys
# input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

m, n = map(int, input().split())
arr = []
for _ in range(n):
	arr.append(list(map(int, input())))

visited = [[0 for _ in range(m)]for _ in range(n)]
q = []
heappush(q,(0,0,0))
while q:
	cost, x, y = heappop(q)
	if(x == n-1 and y == m-1):
		print(cost)
		break
	for d in range(4):
		nx = x + dx[d]
		ny = y + dy[d]
		if 0 <= nx < n and 0 <= ny < m:
			if visited[nx][ny] == 0:
				if arr[nx][ny] == 0:
					heappush(q,(cost,nx,ny))
					visited[nx][ny] = 1
				else:
					heappush(q,(cost+1,nx,ny))
					visited[nx][ny] = 1