# 중간지점, 코스, 리프팅회수, 시작, 끝
def dfs(now, lifting, cnt):
	# print("현재상태")
	# print(now, lifting, cnt)
	global mx
	if(now == t):
		mx = max(mx, cnt)
		# print("컷")
		return
	for el in course[now]:
		# print(el)
		dfs(el[0], lifting, cnt + el[1])
	
	if(lifting > 0 and now > 1):
		for el in lift[now]:
			dfs(el, lifting - 1, cnt)


n, m ,k ,s ,t = map(int,input().split())
course = [[]for _ in range(n+1)]
lift = [[] for _ in range(n+1)]
global mx
mx = -1
for _ in range(m):
	fr, to, length = map(int,input().split())
	course[fr].append([to, length])
	lift[to].append(fr) 
dfs(s,k, 0) # 현재 지점과 남은 리프팅 회수
print(mx)