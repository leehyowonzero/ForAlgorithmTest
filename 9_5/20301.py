from collections import deque

n, k, m = map(int,input().split())
q = deque()
for i in range(1, n+1):
	q.append(i)

d = -1
removed = 0
while(q):
	if(d == -1):
		q.rotate((k-1)*d)
	else:
		q.rotate(k*d)
	print(q.popleft())
	removed += 1
	if(removed %m  == 0):
		d *= -1