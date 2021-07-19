from collections import deque
import math

def checkgoal(x1, y1):
	x2,y2 = 10000, 10000
	dis = math.sqrt(math.pow(x1-x2 , 2) + math.pow(y1-y2, 2))

	return dis
	
def checkdistance(start, end):
	x1,y1 = start[0], start[1]
	x2,y2 = end[0], end[1]
	dis = math.sqrt( math.pow(x1-x2 , 2) + math.pow(y1 - y2 , 2) )
	return dis

def bfs(start, fueltank):
	turn = 0 
	global k
	visited = [0 for _ in range(n)]
	fuel = fueltank * 10
	q = deque()
	q.append(start)
	while(q):
		turncnt = len(q)
		while(turncnt):
			now = q.popleft()
			if(checkgoal(now[0],now[1]) <= fuel and turn <= k):

				return True
			for i in range(n):
				if(visited[i] != 0 or k <= turn):
					continue
				# x, y = layover[i][0], layover[i][1] 	
				# 연료안에 갈 수 있으면 다음 지점을 큐에 넣기
				if(checkdistance(now,layover[i]) < fuel):
					q.append(layover[i])
					visited[i] = 1
			turncnt -= 1
		turn += 1
	return False

global k
n, k = map(int,input().split())
layover = []
for _ in range(n):
	layover.append(list(map(int,input().split())))
# 연료통의 크기
left = 0
right = 10000
while( left <= right):
	mid = (left + right)//2
	print(mid)
	if(bfs([0,0],mid)):
		right = mid - 1
		ans = mid
	else:
		left = mid + 1
print(ans)
