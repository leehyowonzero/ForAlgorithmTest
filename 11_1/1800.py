import heapq
import sys

def bfs(start, limit):
	limitcnt = [sys.maxsize for _ in range(N+1)]
	q = []
	heapq.heappush(q,(start, 0)) # 노드, 리미트 오바된 엣지 갯수
	while q :
		now, nowlimitover  = heapq.heappop(q)
		if(limitcnt[now] < nowlimitover):
			continue
		for next, dist in Edge[now]:
			if(dist > limit):
				if(nowlimitover + 1 < limitcnt[next]):
					limitcnt[next] = nowlimitover + 1
					heapq.heappush(q, (next, nowlimitover + 1))
			else:
				if(nowlimitover < limitcnt[next]):
					limitcnt[next] = nowlimitover
					heapq.heappush(q, (next, nowlimitover))

	if(limitcnt[N] > K):
		return False
	else:
		return True


N, P, K = map(int,input().split())
Edge = [[] for _ in range(N+1)]
for _ in range(P):
	fm, to, dist = map(int,input().split())
	Edge[fm].append((to, dist))
	Edge[to].append((fm, dist))

left = 0
right = 1000001
answer = sys.maxsize

while left <= right:
	mid = (left + right)//2
	flag = bfs(1,mid)
	if flag:
		right = mid -1
		answer = mid
	else:
		left = mid + 1
if answer == sys.maxsize:
	print(-1)
else:
	print(answer)

