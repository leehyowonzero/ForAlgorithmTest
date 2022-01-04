from collections import deque

def check(k, start):
	visited = [0 for _ in range(N)]
	q= deque()
	q.append((start, 1000000001))
	visited[start] = 1000000001
	while q:
		now, mindist = q.popleft()
		for next, dist in Node[now]:
			if(visited[next] != 0):
				continue
			if(mindist > dist ):
				q.append((next, dist))
				visited[next] = dist
			else:
				q.append((next, mindist))
				visited[next] = mindist
	ans = 0
	for el in visited:
		if(el >= k and el != 1000000001):
			ans += 1
	return ans



N, Q = map(int,input().split())
Node = [[] for _ in range(N)]
for _ in range(N-1):
	p, q, r = map(int,input().split())
	Node[p-1].append((q-1, r))
	Node[q-1].append((p-1, r))

for _ in range(Q):
	k, v = map(int,input().split())
	print(check(k, v-1))