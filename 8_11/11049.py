n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
arr = []
for _ in range(n):
	arr.append(list(map(int,input().split())))
if(n == 1):
	print(0)
	exit()
for dis in range(1, n):
	for start in range(n-dis):
		end = start + dis
		dp[start][end] = 2**32
		for k in range(start, end):
			dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] + arr[start][0]* arr[k][1] * arr[end][1])
print(dp[0][n-1])

