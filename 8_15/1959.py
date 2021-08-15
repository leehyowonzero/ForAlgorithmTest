m, n = map(int,input().split())
if(m == 1):
	print(0)
	print(m, n)
	exit()
if(m <= n):
	cycle = m // 2
	m %= 2
	n -= cycle*2
	if(m % 2 == 0): #짝수
		# 마지막 커브 = 2번
		print((cycle-1)*4 + 2)
		print(cycle+1, cycle)
	else:
		print(cycle*4)
		print(cycle+1, cycle + n)

else:
	cycle = n // 2
	n %= 2
	m -= cycle*2
	if(n % 2 == 0):
		print((cycle-1)*4 + 3)
		print(cycle+1, cycle)
	else:
		print(cycle*4 + 1)
		print(cycle+m, cycle+1)

