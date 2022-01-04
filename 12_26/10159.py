n = int(input())
m = int(input())
edge = [[False for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
	heavy, light = map(int,input().split())
	edge[heavy][light] = True
for i in range(n+1):
	edge[i][i] = True
for k in range(n+1):
	for i in range(n+1):
		for j in range(n+1):
			if(edge[i][k] == True and edge[k][j] == True):
				edge[i][j] = True
# edge 배열의 경우 앞인덱스가 뒤인덱스보다 무거우면 트루 
for i in range(1, n+1):
	ans = 0
	for j in range(1, n+1):
		if(edge[i][j] == False and edge[j][i] == False):
			ans += 1
	print(ans)