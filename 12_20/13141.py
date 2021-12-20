def floyd():
	for k in range(1, n+1):
		minedge[k][k] = 0
		for i in range(1, n+1):
			for j in range(1, n+1):
				minedge[i][j] = min(minedge[i][j], minedge[i][k] + minedge[k][j])

maxsize = float('inf')
n, m = map(int,input().split())
minedge = [[maxsize for _ in range(n+1)] for _ in range(n+1)]
maxedge = [[-1 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
	fm, to , value = map(int,input().split())
	minedge[fm][to] = min(minedge[fm][to], value)
	minedge[to][fm] = min(minedge[to][fm], value)
	maxedge[fm][to] = max(maxedge[fm][to], value)
floyd()
ans = maxsize
for startpoint in range(1, n+1): # 브루트포스 점화 시작점 
	caseans = 0
	for i in range(1,n+1):
		for j in range(1,n+1):
			if(maxedge[i][j] != -1):
				caseans = max(caseans,(minedge[startpoint][i] + minedge[startpoint][j] + maxedge[i][j])/2)
				# print(i, j, caseans)
	# print(caseans)
	ans = min(ans, caseans)
	# print()
print(ans)		