from itertools import permutations

def wincheck(score):
	global k
	for i in range(0, 3):
		if(score[i] == k):
			return True
	return False

def dfs(turn, score, cs, nowplayerx, nowplayery, nowhand):
	global ans
	global counter
	global k

	if(nowhand[0] >= n):
		return False
	if(wincheck(score)):
		if(score[0] == k):
			ans = 1
			return True
		else:
			return False
	if(turn == 3*k-2+1):
		return False
	if(counter[cs[nowplayerx][nowhand[nowplayerx]]-1][cs[nowplayery][nowhand[nowplayery]]-1] == 2):
		score[nowplayerx] += 1
		nowhand[nowplayerx] += 1
		nowhand[nowplayery] += 1
		if(wincheck(score)):
			if(score[0] == k):
				ans = 1
				return True
			else:
				return False
		dfs(turn + 1, score, cs, nowplayerx, 3 - nowplayerx- nowplayery,nowhand)
	elif(counter[cs[nowplayerx][nowhand[nowplayerx]]-1][cs[nowplayery][nowhand[nowplayery]]-1] == 1):
		nowhand[nowplayerx] += 1
		nowhand[nowplayery] += 1
		if(nowplayerx < nowplayery):
			score[nowplayery] += 1
			if(wincheck(score)):
				if(score[0] == k):
					ans = 1
					return True
				else:
					return False
			dfs(turn +1, score, cs, nowplayery, 3 - nowplayerx- nowplayery, nowhand)
		else:
			score[nowplayerx] += 1
			if(wincheck(score)):
				if(score[0] == k):
					ans = 1
					return True
				else:
					return False
			dfs(turn +1, score, cs, nowplayerx, 3 - nowplayerx- nowplayery, nowhand)

	elif(counter[cs[nowplayerx][nowhand[nowplayerx]]-1][cs[nowplayery][nowhand[nowplayery]]-1] == 0):
		score[nowplayery] += 1
		nowhand[nowplayerx] += 1
		nowhand[nowplayery] += 1
		if(wincheck(score)):
			if(score[0] == k):
				ans = 1
				return True
			else:
				return False
		dfs(turn +1, score, cs, nowplayery, 3 - nowplayerx- nowplayery, nowhand)
global n
global k
n, k = map(int,input().split())
global counter
counter = []
for i in range(n):
	counter.append(list(map(int,input().split())))
Jiwoo = []
Kyunghee = list(map(int,input().split()))
Minho = list(map(int,input().split()))
global ans
ans = 0
if(k > n):
	print(0)
	exit()
arr = [i for i in range(1, n+1)]
for el in permutations(arr):
	score = [0, 0, 0]
	cs = [list(el), Kyunghee, Minho]
	dfs(0, score, cs, 0, 1,[0,0,0])
	if(ans == 1):
		break

print(ans)
