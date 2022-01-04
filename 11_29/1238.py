import heapq
import sys

input = sys.stdin.readline
INF = float('inf')

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    fm, to, cost = map(int, input().split())
    graph[fm].append((to, cost))


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_idx, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_idx] > cost:
                distance[node_idx] = cost
                heapq.heappush(q, (cost, node_idx))

    return distance


result = 0
backhome = dijkstra(x)
for i in range(1, n + 1):
    gotarget = dijkstra(i)
    result = max(result, gotarget[x] + backhome[i])

print(result)