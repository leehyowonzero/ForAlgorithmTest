t = int(input())
for _ in range(t):
	n = int(input())
	arr = dict()
	a = list(map(int,input().split()))
	for el in a:
		if(el not in arr):
			arr[el] = 1
	m = int(input())
	x = list(map(int,input().split()))
	for el in x:
		if(el in arr):
			print("1")
		else:
			print("0")