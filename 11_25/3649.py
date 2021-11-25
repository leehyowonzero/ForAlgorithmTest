while(True):
	try:
		x = int(input())
		n = int(input())
		arr = []
		for _ in range(n):
			arr.append(int(input()))
		if(n == 0 or n == 1):
			print("danger")
		else:
			x = x * 10000000
			arr.sort()
			leftidx = 0
			rightidx = n-1
			while(leftidx <= rightidx):
				if(leftidx == rightidx):
					print("danger")
					break
				if(arr[leftidx] + arr[rightidx] == x):
					print("yes", arr[leftidx], arr[rightidx])
					break
				elif(arr[leftidx] + arr[rightidx] > x):
					rightidx -= 1
				else:
					leftidx += 1
				
	except:
		break