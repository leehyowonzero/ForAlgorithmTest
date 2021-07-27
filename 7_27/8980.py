n, c = map(int,input().split())
m = int(input())
box = [list(map(int,input().split())) for _ in range(m)]
bus = [c for _ in range(n+1)]
ans = 0
# 빨리 도착하는것부터 담기 담을때마다 그 정류장에 남은 공간 갱신
box.sort(key = lambda x : x[1])
for i in range(m):
	candi = c
	for j in range(box[i][0], box[i][1]):
		candi = min(bus[j], candi)
	candi = min(candi, box[i][2])

	for j in range(box[i][0], box[i][1]):
		bus[j] -= candi
	ans += candi
print(ans)