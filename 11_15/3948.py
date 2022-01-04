dp = [[0 for x in range(21)] for y in range(21)]
dp[0][0] = 1
for i in range(1, 21):
    for j in range(1, 21):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][i - j])
T = int(input())
for _ in range(T):
	n= int(input())
	answer = dp[n][n]
	if(n == 1):
		print(1)
	else:
		print(2*answer)
