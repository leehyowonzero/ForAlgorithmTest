import heapq

n = int(input())
arr = []
for _ in range(n):
	arr.append((list(map(int,input().split()))))
arr.sort()
ans = [0 for _ in range(100001)]
q = [(0, 0)]
for el in arr:
	start, end = el[0], el[1]
	mn, loc = heapq.heappop(q)
	if(mn <= start):
		heapq.heappush(q, (end, loc))
		ans[loc] += 1
	else:
		heapq.heappush(q, (mn, loc))
		heapq.heappush(q, (end, len(q)))
		ans[len(q)-1] += 1
	print(*ans[:len(q)])
print(len(q))
print(*ans[:len(q)])