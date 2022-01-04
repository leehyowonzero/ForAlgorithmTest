import sys
input = sys.stdin.readline
import heapq

# 입력
n = int(input())
people = []
for _ in range(n):
	people.append(list(map(int,input().split())))

# 정렬(start, end 오름차순)
people.sort(key = lambda x : (x[0],x[1]))

# 시작시간이 빠른 사람부터 선
# 선정된 사람보다 빠르게 자리를 뜨는 자리 체크
# 빈 자리가 있다면 앞자리부터 착석
# 없다면 새로운 자리 착석

com = [0 for _ in range(n)]
q = []
allseat = 0
ans = [0 for _ in range(n)]
for person in people:
	start, end = person[0], person[1]
	while(q):
		mn = heapq.heappop(q)
		if(mn[0] < start):
			com[mn[1]] = 0
		else:
			heapq.heappush(q, mn)
			break
	for i in range(allseat + 1):
		if( i == allseat):
			com[i] = 1
			allseat += 1
			heapq.heappush(q,(end, i))
			ans[i] += 1
			break
		if(com[i] == 0):
			com[i] = 1
			heapq.heappush(q, (end, i))
			ans[i] += 1
			break
print(allseat)
print(*ans[:allseat])
	
