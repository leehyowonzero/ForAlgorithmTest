n = int(input())
arr = list(map(int,input().split()))

ans = 0
leftidx = 0
rightidx = n - 1
while(leftidx < rightidx):
	ans = max(ans, min(arr[leftidx],arr[rightidx])*(rightidx-leftidx -1))
	if(arr[leftidx] > arr[rightidx]):
		rightidx -= 1
	else:
		leftidx += 1
print(ans)
