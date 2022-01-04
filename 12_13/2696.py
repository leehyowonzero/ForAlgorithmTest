import heapq

T = int(input())
for _ in range(T):
	m = int(input())
	lenans = m//2 + m%2
	print(lenans)
	arr = []
	loop = m//10
	if(m%10 != 0):
		loop += 1
	for _ in range(loop):
		arr.extend(list(map(int,input().split())))
	midium = arr[0]
	minq = [] #음수로 넣어둬
	maxq = []
	ans = [midium]
	for i in range(1,m):
		if(arr[i] > midium):
			heapq.heappush(maxq,arr[i])
			if(len(maxq) > len(minq) + 1):
				heapq.heappush(minq,-midium)
				midium = heapq.heappop(maxq)
		else:
			heapq.heappush(minq,-arr[i])
			if(len(minq) > len(maxq) + 1):
				heapq.heappush(maxq,midium)
				midium = -heapq.heappop(minq)	

		if(i%2 == 0):
			ans.append(midium)
	loop = lenans//10
	for i in range(loop):
		print(*ans[10*i:10*i + 10])
	print(*ans[10*loop:])