import sys
input  = sys.stdin.readline
import heapq
Inf = float('inf')

def bfsforfox():
	distance = [Inf for _ in range(n+1)]
	distance[1] = 0
	
	heap = []
	heapq.heappush(heap,(0,1))
	while(heap):
		cur_distance, now = heapq.heappop(heap)
		if(cur_distance > distance[now]):
			continue

		for nextnode, dist in nodeforfox[now]:
			w = cur_distance + dist
			if(w < distance[nextnode]):
				distance[nextnode] = w
				heapq.heappush(heap,(w, nextnode))
	return distance


def bfsforwolf():
	distance = [[Inf, Inf] for _ in range(n+1)]
	# distance[1][0] = 0
	distance[1][1] = 0
	
	heap = []
	movetime = 0
	heapq.heappush(heap,(0,1, 0))
	while(heap):
		# print(distance)
		cur_distance, now , movetime = heapq.heappop(heap) # movetime 짝수면 2배 빠르게감
		if(cur_distance > distance[now][(movetime+1)%2]):
			continue
		if(movetime == 0):
			for nextnode, dist in nodeforwolf[now][1]:
				w = cur_distance + dist
				if(w < distance[nextnode][0]):
					distance[nextnode][0] = w
					heapq.heappush(heap,(w, nextnode, 1))
		else:
			for nextnode, dist in nodeforwolf[now][0]:
				w = cur_distance + dist
				if(w < distance[nextnode][1]):
					distance[nextnode][1] = w
					heapq.heappush(heap,(w, nextnode, 0))
			
	return distance


n, m = map(int,input().split())
nodeforfox = [[] for _ in range(n+1)]
nodeforwolf = [[[],[]] for _ in range(n+1)]
for _ in range(m):
	a, b, d = map(int,input().split())
	nodeforfox[a].append([b,2*d])
	nodeforfox[b].append([a,2*d])

	nodeforwolf[a][0].append([b,4*d])
	nodeforwolf[b][0].append([a,4*d])
	nodeforwolf[a][1].append([b,d])
	nodeforwolf[b][1].append([a,d])

foxtime = bfsforfox()
# print(foxtime)
wolftime = bfsforwolf()
# print(wolftime)

ans = 0
for i in range(2, n+1):
	if(foxtime[i] < min(wolftime[i])):
		ans += 1
print(ans)