s = list(input())
n = len(s)
dp = [[0 for _ in range(n)] for _ in range(n)]
for d in range(1, n):
	for i in range(0,n-d):
		j = i + d
		if((s[i] == 'a' and s[j] == 't') or (s[i] == 'g' and s[j] == 'c') ):
			dp[i][j] = dp[i+1][j-1] + 2
		for k in range(i,j):
			dp[i][j] = max(dp[i][j], dp[i][k] + dp[k+1][j])
print(dp[0][n-1])