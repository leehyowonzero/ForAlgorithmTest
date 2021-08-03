# 기본 인덱스별 꿀 양
n = int(input())
arr = [0]
arr.extend(list(map(int,input().split())))
ans = 0
# 왼쪽부터의 누적합
left = [0 for _ in range(n+1)]
for i in range(1,n+1):
	left[i] = left[i-1] + arr[i]
right = [0 for _ in range(n+2)]
for i in range(n,0,-1):
	right[i] = right[i+1] + arr[i]

# 꿀통이 끝에 있는게 유리함
# i = 1 꿀통있는 경우
# i 번에 꿀벌을 선택했을때 + n번에 이미 꿀벌 배치
for i in range(2, n):
	ans = max(ans, right[1] - right[n] + right[1] - arr[i] - right[i])
# i = n 꿀통있는 경우
# i 번에 꿀벌을 선택했을때 + 1번에 이미 꿀벌 배치	
for i in range(2, n):
	ans = max(ans, left[n] - left[1] + left[n] - arr[i] - left[i])
# i 번에 꿀통이 있고 양 사이드에 벌이 있는 경우
for i in range(2,n):
	ans = max(ans,left[i]-arr[1]+right[i]-arr[n])

print(ans)