n = int(input())
arr = []
for _ in range(n):
	arr.append(int(input()))
dp = [[0, 0 ,0] for _ in range(n)] # 0 못먹음 1 그전에 못먹었는데 먹음 2 그전에도 먹었고 이번에도 먹음
dp[0][0] = 0
dp[0][1] = arr[0]
dp[0][2] = 0
for i in range(1, n):
	dp[i][0] = max(dp[i-1][0],dp[i-1][1],dp[i-1][2]) 
	
	if(arr[i] != 0):
		dp[i][1] = dp[i-1][0] + arr[i]
		dp[i][2] = dp[i-1][1] + arr[i]//2
print(max(dp[n-1]))