import copy
dx = [-1,-1,0,1,1,1,0,-1] 
dy = [0,1,1,1,0,-1,-1,-1]

def checkd(arr):
	for i in range(len(arr)):
		arr[i] %= 2
	pivot = arr[0]
	for el in arr:
		if(el != pivot):
			return False
	return True
# 입력
n, m, k = map(int,input().split())
Map  = [[[] for _ in range(n)] for _ in range(n)]
fire = []
for _ in range(m):
	r, c, m, s, d = map(int,input().split())
	fire.append([r-1,c-1,m,s,d])
	Map[r-1][c-1].append([m, s, d])

for _ in range(k):
# 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
	nxtfire = []
	Map  = [[[] for _ in range(n)] for _ in range(n)]
	for el in fire:
		x = el[0]
		y = el[1]
		d = el[4]
		nx = x + dx[d] * el[3]
		ny = y + dy[d] * el[3]
		nxtfire.append([nx%n,ny%n, el[2], el[3], el[4]])
	for el in nxtfire:
		Map[el[0]][el[1]].append(el[2:])
	# 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
	# print(Map)
	nxtfire = []
	for i in range(n):
		for j in range(n):
			# 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
			# 파이어볼은 4개의 파이어볼로 나누어진다.
			# 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
			# 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
			# 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
			# 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
			# 질량이 0인 파이어볼은 소멸되어 없어진다.
			if len(Map[i][j]) >= 2:
				m = 0
				s = 0
				d = []
				cnt = 0
				for el in Map[i][j]:
					m += el[0]
					s += el[1]
					d.append(el[2])
					cnt += 1
				if(checkd(d)):
					d = [0,2,4,6]
				else:
					d = [1,3,5,7]
				m //= 5
				s //= cnt
				if(m != 0):
					for k in range(0,4):
						nxtfire.append([i,j,m,s,d[k]])

			elif len(Map[i][j]) == 1:
				nxtfire.append([i,j, Map[i][j][0][0], Map[i][j][0][1], Map[i][j][0][2]])
	fire = copy.deepcopy(nxtfire)
ans = 0

for el in nxtfire:
	ans += el[2]
print(ans)

