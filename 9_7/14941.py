import bisect
import sys
input = sys.stdin.readline
sieve = [True for _ in range(100001)]

m = int(10**2.5)
for i in range(2, m + 1):
	if( sieve[i] == True):
		for j in range(i+i, 100001, i):
			sieve[j] = False

prime = []
for i in range(2, 100001):
	if sieve[i] == True:
		prime.append(i)

smeven = [0 for _ in range(100001)]
save = 0
for i, el in enumerate(prime):
	if(i%2 == 0):
		smeven[el] = save + el*3
		save = smeven[el]
	else:
		smeven[el] = save - el
		save = smeven[el]
save = 0
for i in range(100001):
	if(smeven[i] == 0):
		smeven[i] = save
	else:
		save = smeven[i]

smodd = [0 for _ in range(100001)]
save = 0
for i, el in enumerate(prime):
	if(i%2 == 0):
		smodd[el] = save - el
		save = smodd[el]
	else:
		smodd[el] = save + el*3
		save = smodd[el]
save = 0
for i in range(100001):
	if(smodd[i] == 0):
		smodd[i] = save
	else:
		save = smodd[i]

n = int(input())
for _ in range(n):
	a, b = map(int,input().split())
	if(bisect.bisect_left(prime,a) %2 == 0):# even
		print(smeven[b]- smeven[a-1])
	else:
		print(smodd[b]- smodd[a-1])
