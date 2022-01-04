import sys 

input = sys.stdin.readline

def dfs(number, cnt):
	global ans
	if(cnt == k):
		ans = max(ans, number)
	for i in range(LEN):
		for j in range(i+1, LEN):
			if(visited[cnt+1][swap(number, i, j)] == 0):
				visited[cnt+1][swap(number, i, j)] = 1
				dfs(swap(number, i, j), cnt+1)

def swap(n, a, b):
	arr = list(str(n))
	arr[a], arr[b] = arr[b], arr[a]
	return int(''.join(arr))

n, k = map(int,input().split())
visited = [[0 for _ in range(10000000)] for _ in range(11)]
global ans
ans = -1
LEN = len(str(n))
dfs(n, 0)
print(ans)