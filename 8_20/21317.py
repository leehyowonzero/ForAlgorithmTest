
n = int(input())
jump = []
for _ in range(n-1):
	jump.append(list(map(int,input().split())))
k = int(input())
if(n == 1):
	print(0)
	exit()
if(n == 2):
	print(jump[0][0])
	exit()
dp = [[100001 for _ in range(2)] for _ in range(n+1)]
dp[0][0] = 0
dp[1][0] = jump[0][0]

for i in range(2, n):
	dp[i][0] = min(dp[i-1][0] + jump[i-1][0] , dp[i-2][0] + jump[i-2][1])
	if(i >= 3):
		dp[i][1] = min(dp[i-1][1]+jump[i-1][0],dp[i-2][1]+jump[i-2][1] , dp[i-3][0] + k)
print(min(dp[n-1][0],dp[n-1][1]))
