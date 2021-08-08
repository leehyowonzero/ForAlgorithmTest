import copy 
from collections import deque
def move(d, ret):
	if d == 0 :
		for i in range(n):
			q = deque()
			k = n-1
			for j in range(n-1,-1,-1):
				q.append(arr[i][j])
				arr[i][j] = 0
				if(len(q) > 1):
					left = q.popleft()
					if(left == 0):
						continue
					else:
						if(left == q[0]):
							q.popleft()
							arr[i][k] = left * 2
						else:
							arr[i][k] = left
						ret = max(ret, arr[i][k])
						k += -1
			if(q):
				arr[i][k] = q.popleft()
				ret = max(ret, arr[i][k])

	if d == 1 :
		for i in range(n):
			q = deque()
			k = 0
			for j in range(0,n):
				q.append(arr[i][j])
				arr[i][j] = 0
				if(len(q) > 1):
					left = q.popleft()
					if(left == 0):
						continue
					else:
						if(left == q[0]):
							q.popleft()
							arr[i][k] = left * 2
						else:
							arr[i][k] = left
						ret = max(ret, arr[i][k])
						k += 1
						
			if(q):
				arr[i][k] = q.popleft()
				ret = max(ret, arr[i][k])
	if d == 2 :	
		for j in range(n):
			q = deque()
			k = 0
			for i in range(0,n):
				q.append(arr[i][j])
				arr[i][j] = 0
				if(len(q) > 1):
					left = q.popleft()
					if(left == 0):
						continue
					else:
						if(left == q[0]):
							q.popleft()
							arr[k][j] = left * 2
						else:
							arr[k][j] = left
						ret = max(ret, arr[k][j])
						k += 1
			if(q):
				arr[k][j] = q.popleft()
				ret = max(ret, arr[k][j])
	if d == 3 :
		for j in range(n):
			q = deque()
			k = n-1
			for i in range(n-1,-1,-1):
				q.append(arr[i][j])
				arr[i][j] = 0
				if(len(q) > 1):
					left = q.popleft()
					if(left == 0):
						continue
					else:
						if(left == q[0]):
							q.popleft()
							arr[k][j] = left * 2
						else:
							arr[k][j] = left
						ret = max(ret, arr[k][j])
						k += -1
			if(q):
				arr[k][j] = q.popleft()
				ret = max(ret, arr[k][j])
	return ret

def dfs(cnt,nowmax):
	global arr
	global ans

	# for i in range(n):
	# 	for j in range(n):
	# 		print(arr[i][j], end = " ")
	# 	print()
	# print()
	ans = max(nowmax, ans)
	if(cnt == 10):
		return
	if(nowmax * (2**(10-cnt)) <= ans):
		# print(cnt, "이걸론안되죠")
		return
	# print(nowmax)
	
	
	temp = copy.deepcopy(arr)
	for i in range(4):
		nowmax = move(i,nowmax)
		if(temp == arr):
			continue
		dfs(cnt+1, nowmax)
		arr = copy.deepcopy(temp)

n = int(input())
arr = []
for _ in range(n):
	arr.append(list(map(int,input().split())))
ans = 0
nowmax= 0
for i in range(n):
	for j in range(n):
		nowmax = max(nowmax, arr[i][j])
dfs(0, nowmax)
print(ans)

