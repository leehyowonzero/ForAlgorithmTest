# 구글링 참고

import sys
input = sys.stdin.readline

def check(x, y, k):
	for i in range(x, x+k+1):
		for j in range(y, y+k+1):
			if(arr[i][j] == 0):
				return False
	return True
def change(x, y, k):
	for i in range(x, x+k+1):
		for j in range(y, y+k+1):
			if(arr[i][j] == 1):
				arr[i][j] = 0
			else:
				arr[i][j] = 1

def dfs(x, y, cnt):
	global answer
	if(y >= 10):
		answer = min(answer, cnt)
		return
	if(x >= 10):
		dfs(0, y+1, cnt)
		return
	if(arr[x][y] == 0):
		dfs(x+1,y,cnt)
	else: # 색종이를 붙일 수 있는 공간일 때
		for k in range(5):
			if(usedpaper[k] == 5):
				continue
			if(x + k >= 10 or y + k >= 10):
				continue
			if not(check(x, y, k)):
				continue
			else:
				change(x, y, k)
				usedpaper[k] += 1
				dfs(x+k+1, y, cnt +1)
				change(x, y, k)
				usedpaper[k] -= 1




arr = []
for _ in range(10):
	arr.append(list(map(int,input().split())))

usedpaper = [0 for _ in range(5)]
answer = sys.maxsize
dfs(0, 0, 0)
if(answer == sys.maxsize ):
	print(-1)
else:
	print(answer)
