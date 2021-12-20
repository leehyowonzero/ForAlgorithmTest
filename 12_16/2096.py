n = int(input())
dp = [[[0, 0] for _ in range(3)] for _ in range(2)]

for _ in range(1):
	arr = list(map(int,input().split()))
	for i in range(3):
		dp[0][i][0] = arr[i]
		dp[0][i][1] = arr[i]
for i in range(1,n):
	arr = list(map(int,input().split()))
	for j in range(3):
		if j == 0:
			dp[1][j][0] = max(dp[0][j][0],dp[0][j+1][0]) + arr[j]
			dp[1][j][1] = min(dp[0][j][1],dp[0][j+1][1]) + arr[j]
		elif j == 1:
			dp[1][j][0] = max(dp[0][j-1][0],dp[0][j][0],dp[0][j+1][0]) + arr[j]
			dp[1][j][1] = min(dp[0][j-1][1],dp[0][j][1],dp[0][j+1][1]) + arr[j]
		else:
			dp[1][j][0] = max(dp[0][j-1][0],dp[0][j][0]) + arr[j]
			dp[1][j][1] = min(dp[0][j-1][1],dp[0][j][1]) + arr[j]
	for j in range(3):
		dp[0][j][0] = dp[1][j][0]
		dp[0][j][1] = dp[1][j][1]
print(max(dp[0][0][0],dp[0][1][0],dp[0][2][0]), end = ' ')
print(min(dp[0][0][1],dp[0][1][1],dp[0][2][1]))