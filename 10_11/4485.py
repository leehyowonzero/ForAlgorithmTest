import sys
input = sys.stdin.readline
import heapq

Inf = float('inf')

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
	visited = [[Inf for _ in range(n)] for _ in range(n)]
	heap = []
	heapq.heappush(heap,(arr[x][y],x,y))
	visited[0][0] = arr[0][0]
	while(heap):
		w, x, y = heapq.heappop(heap)
		for d in range(0, 4):
			nx = x + dx[d]
			ny = y + dy[d]
			if not (0<=nx<n and 0<=ny<n):
				continue
			if(visited[nx][ny] > arr[nx][ny] + w):
				visited[nx][ny] = arr[nx][ny] + w
				heapq.heappush(heap,(arr[nx][ny] + w,nx,ny))
	return visited[n-1][n-1]
i = 0
while(True):
	i += 1 
	n = int(input())
	if(n == 0):
		break
	arr = []
	for _ in range(n):
		arr.append(list(map(int,input().split())))
	print("Problem %d: %d" %(i, bfs(0,0)))

