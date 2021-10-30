M, N = map(int,input().split())
sm = [0 for _ in range(2*M-1)]
ans = [[ 1 for _ in range(M)] for _ in range(M)]
for _ in range(N):
	arr = list(map(int,input().split()))
	j = 0
	for i, el in enumerate(arr):
		for _ in range(el):
			sm[j] += i
			j += 1
j = 0
for i in range(M-1, -1 ,-1):
	ans[i][0] += sm[j]
	j += 1
for i in range(1, M):
	ans[0][i] += sm[j]
	j += 1
for i in range(1,M):
	for j in range(1, M):
		ans[i][j] = ans[i-1][j]
for i in range(M):
	print(*ans[i])