import sys

sys.setrecursionlimit(10001)

def dfs(cur): 
	visited[cur] = 1 
	for u in node[cur]: 
		if not visited[u]: 
			dfs(u) 
			dp[cur][1] += dp[u][0]  
			dp[cur][0] += max(dp[u][0], dp[u][1]) 

n = int(input())
village = [0]
village.extend(list(map(int,input().split())))
dp = [[0, village[i]] for i in range(n+1)]
node = [[] for _ in range(n+1)]
for _ in range(n-1):
	v, u = map(int, input().split()) 
	node[v].append(u) 
	node[u].append(v)

visited = [0 for _ in range(n+1)]
dfs(1)
print(max(dp[1][0], dp[1][1]))

