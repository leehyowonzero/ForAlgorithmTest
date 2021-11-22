import heapq
import sys

input = sys.stdin.readline
def calc(arr):
	q = []
	for el in arr:
		heapq.heappush(q,el)
	ret = 1
	while(len(q) > 1):
		x = heapq.heappop(q)
		y = heapq.heappop(q)
		tmp = x*y
		heapq.heappush(q, tmp)
		ret = ret * tmp 
	return ret%(10**9 + 7)
	


T = int(input())
for _ in range(T):
	n = int(input())
	arr = list(map(int,input().split()))
	ans = calc(arr)
	print(ans)