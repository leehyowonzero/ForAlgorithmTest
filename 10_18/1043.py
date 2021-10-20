from collections import deque

n, m = map(int, input().split())
notlier = list(map(int, input().split()))[1:]
graph = [list(map(int, input().split()))[1:] for _ in range(m)]

node = [False for _ in range(n+1)]
party = [False for _ in range(m)]

for el in notlier:
	queue = deque()
	queue.append(el)
	node[el] = True

	while queue:
		value = queue.popleft()
		for i in range(len(graph)):
			if value in graph[i]:
				for j in graph[i]:
					if not node[j]:
						queue.append(j)
						node[j] = True
				party[i] = True

print(party.count(False))