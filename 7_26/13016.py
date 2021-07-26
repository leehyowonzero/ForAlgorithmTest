import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

def dfs(pos, length, visited):
	global maxDis, maxDis2
	global mx_len
	global end_point
	if(visited[pos] == 1):
		return
	visited[pos] = 1
	maxDis[pos] = length

	if(mx_len < length):
		end_point = pos
		mx_len = length
	
	for i in range(len(node[pos])):
		dfs(node[pos][i][0], length + node[pos][i][1], visited)
	visited[pos] = 0

# 입력
global mx_len
global end_point
global maxDis, maxDis2
n = int(input())
visited = [0 for _ in range(n+1)]
node = [[] for _ in range(n+1)]
maxDis = [0 for _ in range(n+1)]
maxDis2 = [0 for _ in range(n+1)]
mx_len = 0
for i in range(n-1):
	fr, to, length = map(int,input().split())
	node[fr].append([to, length])
	node[to].append([fr, length])

dfs(1, 0, visited)
start_point = end_point
mx_len = 0
dfs(start_point, 0, visited)
for i in range(1,n+1):
	maxDis2[i] = maxDis[i];
	maxDis[i] = 0

dfs(end_point, 0 ,visited)
for i in range(1, n+1):
	print(max(maxDis[i], maxDis2[i]))