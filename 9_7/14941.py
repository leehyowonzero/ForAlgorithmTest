def prime():
	sieve = [True for _ in range(10**5+1)]

	m = int(10**2.5)
	for i in range(2, m + 1):
		if( sieve[i] == True):
			for j in range(i+i, 10**5, i):
				sieve[j] = False
	
	return [i for i in range(2, 10**5) if sieve[i] == True]

prime = prime()
primecnt = [0 for _ in range(10**5+1)]
for el in prime:
	primecnt[el] += 1
for i in range(0, 10**5):
	primecnt[i+1] = primecnt[i+1] + primecnt[i]
# print(primecnt)

n = int(input())
for _ in range(n):
	ans = 0
	a, b = map(int,input().split())
	for cnt, i in enumerate(range(primecnt[a],primecnt[b]+1)):
		if(i == 0):
			continue
		if(cnt % 2 == 0):
			ans += prime[i-1] * 3 
		else:
			ans -= prime[i-1]
	print(ans)