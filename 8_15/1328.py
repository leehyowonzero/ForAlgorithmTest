def building(n, l, r):
	if(n < 1):
		return 0
	if( l == 0 or r == 0):
		return 0
	if(n == 1 ):
		if(l > 1 or r > 1):
			return 0
		else:
			return 1
	# print(n, l , r)
	if(dp[n][l][r] != -1):
		return dp[n][l][r]
	dp[n][l][r] = ((n-2)*building(n-1,l,r) + building(n-1,l-1,r) + building(n-1,l,r-1)) % 1000000007
	return dp[n][l][r]
n, l , r = map(int,input().split())
dp = [[[-1 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
print(building(n, l , r))