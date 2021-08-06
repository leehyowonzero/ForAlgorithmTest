def check(a, b):
	global ans
	now = arr[0]
	for el in arr[1:]:
		if el == a*now + b:
			now = el
		else:
			return False
	ans.append(now*a + b)
	return True

n= int(input())
arr = list(map(int,input().split()))
if(n == 1):
	print("A")
elif(n == 2):
	if(arr[0] == arr[1]):
		print(arr[0])
	else:
		print("A")
else:
	ans = []
	if arr[1] == arr[0]:
		a = 0
	else:
		a = (arr[1] - arr[2]) // (arr[0] - arr[1])
	b = arr[1] - arr[0] * a
	check(a,b)
	ans = list(set(ans))
	if (len(ans) == 0):
		print("B")
	elif(len(ans) == 1):
		print(ans[0])
	else:
		print("A")
