n, m = map(int, input().split())
d = dict()
ans = 0
for _ in range(n):
	d[input()] = 1
for _ in range(m):
	if(input() in d):
		ans += 1
print(ans)