import sys
input = sys.stdin.readline

n, k = map(int,input().split())
if(n == 1):
	print("0")
	exit()
dp = [0 for _ in range(n+1)]
dp[1] = 1
dp[2] = 1
for i in range(3,n+1):
	dp[i] = (dp[i-1] + 2*dp[i-2])%1000000007
ans = 0
for i in range(1,n-1):
	ans += dp[i] # 오른쪽

# 왼쪽
ans += dp[n-k]
for i in range(n-2, n-k-1,-1):
	ans += dp[i]
print(ans%1000000007)