import bisect

n, h = map(int,input().split())
arr = [0 for _ in range(n+1)]
for i in range(1,n+1):
	arr[i] = int(input())
ans = [0 for _ in range(h)]
# 홀수는 밑에서나고 짝수는 위에서 내려옴
# 홀수
bottom = []
for i in range(1,n+1,2):
	bottom.append(arr[i])
bottom.sort()

# 짝수
top = []
for i in range(2,n+1,2):
	top.append(arr[i])
top.sort()
# 모든 경우의수를 보면서 각각 누적합을 구하여 가장 작은 벽을 뚫을때의 누적합을 출력 
ans = 0
mn = n
for i in range(1, h+1):
	if (n-(bisect.bisect_left(bottom,i)+bisect.bisect_left(top,h-i+1)) < mn):
		mn = n-(bisect.bisect_left(bottom,i)+bisect.bisect_left(top,h-i+1))
		ans = 1
	elif(n-(bisect.bisect_left(bottom,i)+bisect.bisect_left(top,h-i+1)) ==  mn):
		ans +=1

print(mn, ans)

