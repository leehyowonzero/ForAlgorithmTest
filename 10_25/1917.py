import sys
input = sys.stdin.readline

def check4(arr):
	for i in range(1,5): # 첫째 마지막 줄 빼고
		if(arr[i].count(1) == 4):
			if(arr[i-1].count(1) and arr[i+1].count(1)): # 위아래 1개씩 붙어있는 경우
				return True
	return False

def check3(arr):
	for i in range(1,5): # 첫째 마지막 줄 빼고
		if(arr[i].count(1) == 3):
			if(arr[i-1].count(1) == 2 and arr[i+1].count(1) == 1): # 위아래 2개 1개씩인데 1개는 상관없이 붙기만하면되고 2개 붙은 놈은 꽁지에 붙어있어야한다.
				cnt = 0
				for j in range(6):
					if(arr[i-1][j] == 1 and arr[i][j] == 1):
						cnt += 1
				if(cnt == 1):
					return True
			if(arr[i+1].count(1) == 2 and arr[i-1].count(1) == 1): # 위아래 2개 1개씩인데 1개는 상관없이 붙기만하면되고 2개 붙은 놈은 꽁지에 붙어있어야한다.
				cnt = 0
				for j in range(6):
					if(arr[i+1][j] == 1 and arr[i][j] == 1):
						cnt += 1
				if(cnt == 1):
					return True
	for i in range(0,5):
		if(arr[i].count(1) == 3 and arr[i+1].count(1) == 3):
			cnt = 0
			for j in range(6):
				if(arr[i][j] == 1 and arr[i+1][j] == 1):
					cnt +=1
			if(cnt == 1):
				return True
	return False

def check2(arr):
	for i in range(0,4):
		if(arr[i].count(1) == 2 and arr[i+1].count(1) == 2 and arr[i+2].count(1) == 2):
			# 돌려서 체크했을때 2개 붙어있는게 2쌍 나오면 오케이
			cnt = 0
			rotatedarr = [[arr[x][y] for x in range(6)] for y in range(6)]
			for j in range(0, 6):
				if(rotatedarr[j].count(1) == 2):
					cnt += 1 
			if(cnt == 2):
				return True
	return False


for _ in range(3):
	planar = [list(map(int,input().split())) for _ in range(6)]
	rotatedplanar = [[planar[x][y] for x in range(6)] for y in range(6)]
	if(check4(planar)):
		print("yes")
		continue
	if(check3(planar)):
		print("yes")
		continue
	if(check2(planar)):
		print("yes")
		continue
	if(check4(rotatedplanar)):
		print("yes")
		continue
	if(check3(rotatedplanar)):
		print("yes")
		continue
	if(check2(rotatedplanar)):
		print("yes")
		continue
	print("no")