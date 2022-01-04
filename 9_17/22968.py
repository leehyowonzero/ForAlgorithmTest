dp = [0 for _ in range(50)]
dp[1] = 1
dp[2] = 2
for i in range(3, 50):
	dp[i] = 1 + dp[i-1] + dp[i-2]
n = int(input())
for _ in range(n):
	x = int(input())
	for i in range(0, 50):
		if(x < dp[i]):
			print(i-1)
			break