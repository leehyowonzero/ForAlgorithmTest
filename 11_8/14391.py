def Calc(checkarr):
	# 행검사
	ans = 0
	for i in range(n):
		now = 0
		for j in range(m):
			if(checkarr[i][j] == '0'):
				now *= 10
				now += arr[i][j]
			else:
				ans += now
				now = 0
		ans += now
	for i in range(m):
		now = 0
		for j in range(n):
			if(checkarr[j][i] == '1'):
				now *= 10
				now += arr[j][i]
			else:
				ans += now
				now = 0
		ans += now
	return ans


n, m = map(int,input().split())
arr = []
for _ in range(n):
	arr.append(list(map(int,list(input()))))

number = 2**(n*m)
answer= 0
for i in range(0, number): # 모든 경우의 수
	case = bin(i)[2:]
	while len(case) < n*m:
		case = '0'+ case 
	# print(case)
	checkarr = [[None for _ in range(m)] for _ in range(n)]
	for i in range(n*m):
		checkarr[i//m][i%m] = case[i]
	answer = max(answer,Calc(checkarr))
print(answer)