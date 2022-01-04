n, k = map(int,input().split())
x = n
for i in range(1, k+1):
	rest = x % k
	if(rest == 0):
		print(i)
		exit(0)
	x = int(''.join([str(rest),str(n)]))
print(-1)