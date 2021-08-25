from collections import deque

n = int(input())
arr = list(map(int,input().split()))
q = deque()
ans = [0 for _ in range(n+1)]
for i in range(n):
	el = arr[i]
	while True:
		if(len(q) == 0):
			break
		if(q[-1][1] > el):
			ans[i+1] = q[-1][0]+1
			break
		q.pop()
	q.append([i, el])
print(*ans[1:])