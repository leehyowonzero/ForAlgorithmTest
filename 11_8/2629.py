n = int(input())
weight = list(map(int,input().split()))
beadnum = int(input())
bead = list(map(int,input().split()))

visited = [False for _ in range(0, 40001)]
visited[0] = True

# 모든 추를 활용하여 더해서 만들 수 있는 visited 배열
for el in weight:
	for i, x in enumerate(visited[:]):
		if(x == True and i + el  < 40001):
			visited[i+el] = True

# 모든 추를 활용하여 빼면서 만들 수 있는 visited 배열
for el in weight:
	for i, x in enumerate(visited[:]):
		if(x == True and i - el  > 0):
			visited[i-el] = True

for el in bead:
	if(visited[el] == True):
		print("Y")
	else:
		print("N")