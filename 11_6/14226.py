import heapq

S = int(input())

dp = [[0 for _ in range(1001)] for _ in range(1001)]
q = []
heapq.heappush(q, (0, [1,0]))

while(q):
	w, el = heapq.heappop(q)
	if(el[0] == S):
		print(w)
		break
	if(dp[el[0]][el[0]] == 0):
		dp[el[0]][el[0]] = w + 1
		heapq.heappush(q, (w+1, [el[0],el[0]]))
	if( el[0]+el[1] < 1001 and dp[el[0]+el[1]][el[1]] == 0):
		dp[el[0]+el[1]][el[1]] = w + 1
		heapq.heappush(q, (w+1, [el[0]+el[1],el[1]]))
	if(el[0]-1 >= 0 and dp[el[0]-1][el[1]] == 0):
		dp[el[0]-1][el[1]] = w + 1
		heapq.heappush(q, (w+1, [el[0]-1,el[1]]))