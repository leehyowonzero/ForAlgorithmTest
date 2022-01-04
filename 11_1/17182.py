import sys

def dfs(start, cnt, dist):
	global ans
	if cnt == N:
		ans = min(ans, dist)
	
	for i in range(N):
		if not(visited[i]): #방문한 적이 없으면
			visited[i] = True
			dfs(i, cnt + 1, dist + graph[start][i])
			visited[i] = False


N, K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
ans = sys.maxsize

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j : continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

visited = [False for _ in range(N)]
visited[K] = True
dfs(K, 1, 0)
print(ans)