n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
if(n == 1):
	print(0)
	exit()
ans = sensor[-1] - sensor[0]
arr = []
for i in range(len(sensor)-1):
	arr.append(sensor[i+1] - sensor[i])
arr.sort(reverse = True)
for i in range(k-1):
	ans -= arr[i]
print(ans)