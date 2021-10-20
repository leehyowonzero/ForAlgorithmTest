import heapq
import sys
input = sys.stdin.readline

n = int(input())

left = []
right = []

for _ in range(n):
	x = int(input())
	if(len(left) == len(right)):
		heapq.heappush(left,x)
	else:
		heapq.heappush(right,-x) # 음수로 넣기
	
	if(len(left) >= 1 and len(right) >= 1):
		if(left[0] > right[0]*-1):
			heapq.heappush(right,-heapq.heappop(left))
			heapq.heappush(left,-heapq.heappop(right))
	ans = heapq.heappop(left)
	print(ans)
	heapq.heappush(left,ans)
	