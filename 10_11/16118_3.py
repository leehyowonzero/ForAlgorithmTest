import sys
input  = sys.stdin.readline
Inf = int(1e9)
from heapq import heappush, heappop


def bfsforfox():
	distance = [Inf for _ in range(n+1)]
	distance[1] = 0
	
	heap = []
	heappush(heap,(0,1))
	while(heap):
		cur_distance, now = heappop(heap)
		if(cur_distance > distance[now]):
			continue
		
		for nextnode, dist in node[now]:
			w = cur_distance + dist
			if(w < distance[nextnode]):
				distance[nextnode] = w
				heappush(heap,(w, nextnode))
	return distance


def bfsforwolf():
	distance = [[Inf, Inf] for _ in range(n+1)]
	distance[1][1] = 0
	
	heap = []
	movetime = 0
	heappush(heap,(0,1, 0))
	while(heap):
		cur_distance, now , movetime = heappop(heap)
		if(cur_distance > distance[now][(movetime+1)%2]):
			continue
		for nextnode, dist in node[now]:
			if(movetime == 0):
				w = cur_distance + dist//2
				if(w < distance[nextnode][0]):
					distance[nextnode][0] = w
					heappush(heap,(w, nextnode, 1))
			else:
				w = cur_distance + dist*2
				if(w < distance[nextnode][1]):
					distance[nextnode][1] = w
					heappush(heap,(w, nextnode, 0))
			
	return distance


n, m = map(int,input().split())
node = [[] for _ in range(n+1)]
for _ in range(m):
	a, b, d = map(int,input().split())
	node[a].append((b,2*d))
	node[b].append((a,2*d))
foxtime = bfsforfox()
# print(foxtime)
wolftime = bfsforwolf()
# print(wolftime)

ans = 0
for i in range(2, n+1):
	if(foxtime[i] < min(wolftime[i])):
		ans += 1
print(ans)